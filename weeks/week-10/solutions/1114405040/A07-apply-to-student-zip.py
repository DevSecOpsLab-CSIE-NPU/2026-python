# A07. 綜合應用：把 I/O 技巧套到真實學生資料
# Bloom: Apply — 複習並組合 R01~A06 的 API
#
# 資料來源：assets/npu-stu-109-114-anon.zip（6 屆新生資料庫，學號已匿名）
# 用到的小節對照：
#   5.11 pathlib 組路徑
#   5.12 exists 檢查
#   5.7  zipfile 讀壓縮檔（不解壓）
#   5.1  encoding='utf-8-sig' 處理 Excel 存的 BOM
#   5.6  io.StringIO 把 bytes 轉成 csv 可讀的 file-like
#   5.19 TemporaryDirectory 沙箱輸出
#   5.5  open(..., 'x') 只寫一次的報告檔
#   5.21 pickle 保存跨屆統計快照
#   5.2  print(file=) 寫 Markdown 週報

import csv
import io
import pickle
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

# ── 找到資料檔位置 ────────────────────────────────────
# 以目前腳本所在位置為基準，往上回到專案根目錄，再往 assets 找 ZIP。
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


# ── 不解壓縮，直接讀取 ZIP 內的 CSV ───────────────────
# 這個函式會逐年產生 (年度, header, rows)，讓後面的統計可以一屆一屆處理。
def iter_year_csv(zip_path: Path):
    """逐年產生 (年度, header, rows)。"""
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            # 只處理 CSV 檔，其它檔案直接跳過。
            name = info.filename
            if not name.endswith(".csv"):
                continue
            # 檔名開頭通常就是學年，例如 109、110、111...
            year = name[:3]

            # 先讀成 bytes，再轉成文字並去掉 Excel 常見的 BOM。
            raw = z.read(info)
            text = raw.decode("utf-8-sig")
            # 用 StringIO 把字串包成檔案型物件，方便 csv.reader 直接使用。
            reader = csv.reader(io.StringIO(text))
            rows = list(reader)
            yield year, rows[0], rows[1:]


# ── 跨屆統計 ───────────────────────────────────────────
# summary 會存每一屆的總人數、系所分布、入學方式分布。
summary = {}
all_depts = Counter()

for year, header, rows in iter_year_csv(ZIP_PATH):
    # 從表頭找出需要的欄位位置。
    dept_idx = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    # 用 Counter 統計每屆各系所與各入學方式的人數。
    by_dept = Counter(r[dept_idx] for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    summary[year] = {
        "total": len(rows),
        "by_dept": by_dept,
        "by_entry": by_entry,
    }
    all_depts.update(by_dept)

# ── 終端輸出：總覽 ─────────────────────────────────────
# 先列出每屆總人數，再印出累計熱門系所與 114 學年的入學方式分布。
print("\n=== 6 屆新生人數 ===")
for year in sorted(summary):
    print(f"  {year} 學年：{summary[year]['total']:>4} 人")

print("\n=== 全體最熱門 5 個系所（累計 6 屆） ===")
for dept, n in all_depts.most_common(5):
    print(f"  {n:>4} 人  {dept}")

print("\n=== 114 學年入學方式分布 ===")
for kind, n in summary["114"]["by_entry"].most_common():
    print(f"  {n:>4} 人  {kind}")


# ── 在沙箱中產生報告與快照，避免污染專案目錄 ─────────
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)

    # 用 pickle 把整個 summary 存成快照，之後可以直接載入重用。
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:
        pickle.dump(summary, f)
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 用 'x' 模式建立 Markdown 檔，若檔案已存在就會報錯，不會覆蓋。
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:
        print("# 6 屆新生概況報告\n", file=f)
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)
        for year in sorted(summary):
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(f"| {year} | {summary[year]['total']} | "
                  f"{top_dept} ({top_n}) |", file=f)

    # 把 Markdown 報告讀回來，直接印到終端機預覽。
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # 驗證 pickle 可以正常反序列化，確認快照內容可讀。
    with open(snap, "rb") as f:
        loaded = pickle.load(f)
    print("pickle 讀回 key:", sorted(loaded.keys()))

# 離開 with 之後，TemporaryDirectory 會自動清掉暫存資料。
print("\n(沙箱已自動清理)")


# ── 延伸挑戰：可以自行嘗試的變化 ───────────────────────
# 1) 把報告改寫到 HERE / 'report.md'（改用 'w' 模式會覆蓋，'x' 會報錯）。
# 2) 加一欄「女性比例」：找出性別欄位後用 Counter 統計。
# 3) 把 summary 壓縮存成 summary.pkl.gz（gzip.open('wb') + pickle.dump）。
# 4) 跨屆找出「人數逐年下降最明顯」的系所（需要把 by_dept 按年排成折線）。
