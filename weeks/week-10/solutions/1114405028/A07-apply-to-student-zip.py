# A07-apply-to-student-zip.py
# 完整繁體中文註釋版：把 I/O 技巧套到學生資料壓縮檔，做跨屆統計與報告

import csv
import io
import pickle
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

# ── 5.11 / 5.12 定位資料檔案並驗證存在 ─────────────────────────────
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


# ── 5.7 + 5.6 + 5.1 讀取 ZIP 裡的 CSV，不解壓檔案 ──────────────
def iter_year_csv(zip_path: Path):
    """逐年 yield (年度, header, rows)。"""
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            # 檔案清單中只處理 .csv 檔案
            name = info.filename
            if not name.endswith(".csv"):
                continue
            year = name[:3]  # 例如 '109'、'110'...

            raw = z.read(info)                       # 讀出 bytes
            text = raw.decode("utf-8-sig")           # 處理 Excel CSV 常見的 BOM
            reader = csv.reader(io.StringIO(text))   # StringIO 當作 file-like 物件
            rows = list(reader)
            yield year, rows[0], rows[1:]


# ── 跨屆統計：每年度總人數、系所與入學方式分布 ─────────────────
summary = {}        # 儲存每年度統計結果
all_depts = Counter()

for year, header, rows in iter_year_csv(ZIP_PATH):
    dept_idx = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    by_dept = Counter(r[dept_idx] for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    summary[year] = {
        "total": len(rows),
        "by_dept": by_dept,
        "by_entry": by_entry,
    }
    all_depts.update(by_dept)

# ── 直接在終端輸出統計報告 ───────────────────────────────────
print("\n=== 6 屆新生人數 ===")
for year in sorted(summary):
    print(f"  {year} 學年：{summary[year]['total']:>4} 人")

print("\n=== 全體最熱門 5 個系所（累計 6 屆） ===")
for dept, n in all_depts.most_common(5):
    print(f"  {n:>4} 人  {dept}")

print("\n=== 114 學年入學方式分布 ===")
for kind, n in summary["114"]["by_entry"].most_common():
    print(f"  {n:>4} 人  {kind}")


# ── 5.19 + 5.5 + 5.2 + 5.21：在暫存資料夾中產生報告與快照 ─────────
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)

    # 5.21 將 summary 序列化成 pickle，方便日後直接讀回
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:
        pickle.dump(summary, f)
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 5.5 使用 'x' 模式建立報告檔，避免覆蓋同名檔案
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:
        print("# 6 屆新生概況報告\n", file=f)
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)
        for year in sorted(summary):
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(f"| {year} | {summary[year]['total']} | {top_dept} ({top_n}) |", file=f)

    # 讀回生成的 Markdown 報告內容進行預覽
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # 驗證 pickle 讀回是否正確
    with open(snap, "rb") as f:
        loaded = pickle.load(f)
    print("pickle 讀回 key:", sorted(loaded.keys()))

# 離開 TemporaryDirectory 之後，暫存資料夾與其內容會自動被刪除
print("\n(沙箱已自動清理)")


# ── 課堂延伸挑戰 ─────────────────────────────────────
# 1) 把報告改寫到 HERE / 'report.md'，改用 'w' 模式會覆蓋，'x' 模式會在檔案存在時報錯。
# 2) 加一欄「女性比例」，先找出性別欄位後用 Counter 統計。
# 3) 把 summary 壓縮存成 summary.pkl.gz：gzip.open('scores.pkl.gz','wb')。
# 4) 跨屆找出「人數逐年下降最明顯」的系所。
