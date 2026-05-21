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

# 這個作業示範如何把多種 I/O 技巧組合起來：
# - 不解壓 zip 檔直接讀 CSV
# - 處理 UTF-8 BOM
# - 用 Counter 做統計
# - 用 TemporaryDirectory 做沙箱輸出
# - 用 pickle 保存快照

# ── 5.11 / 5.12 找到資料檔 ─────────────────────────────
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


# ── 5.7 + 5.6 + 5.1 不解壓讀 zip 裡的 CSV ──────────────
def iter_year_csv(zip_path: Path):
    """逐年讀取 zip 檔中的 CSV 檔案，回傳 (年度, header, rows)。

    這裡不會把整個 zip 解壓到硬碟，而是直接在記憶體裡讀取每個 CSV。
    """
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            # 只處理 CSV 檔案，忽略其他可能的檔案
            name = info.filename
            if not name.endswith(".csv"):
                continue

            # 假設檔名開頭是學年，例如 '109.csv'、'110.csv'
            year = name[:3]  # '109'~'114'

            # 直接讀出壓縮檔內的 bytes，不解壓到實體檔案
            raw = z.read(info)                       # bytes
            # Excel 存成 CSV 時常會帶 UTF-8 BOM，decode('utf-8-sig') 會自動去除
            text = raw.decode("utf-8-sig")
            # StringIO 可以把字串轉成類檔物件，讓 csv.reader 可以讀取
            reader = csv.reader(io.StringIO(text))   # 5.6 StringIO 當檔
            rows = list(reader)

            # 第一列是 header，後面才是真正的資料列
            yield year, rows[0], rows[1:]


# ── 跨屆統計 ───────────────────────────────────────────
summary = {}        # {年度: {'total': n, 'by_dept': Counter, 'by_entry': Counter}}
all_depts = Counter()  # 累計 6 屆所有系所的人數

for year, header, rows in iter_year_csv(ZIP_PATH):
    # 找出欄位在 header 中的位置
    dept_idx  = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    # 過濾掉欄位不足的列，避免直接存取時發生 IndexError
    by_dept  = Counter(r[dept_idx]  for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    summary[year] = {
        "total":    len(rows),
        "by_dept":  by_dept,
        "by_entry": by_entry,
    }
    # 累積所有學年度的系所計數，後續可以找出熱門系所
    all_depts.update(by_dept)

# ── 終端輸出：總覽 ─────────────────────────────────────
print("\n=== 6 屆新生人數 ===")
for year in sorted(summary):
    print(f"  {year} 學年：{summary[year]['total']:>4} 人")

print("\n=== 全體最熱門 5 個系所（累計 6 屆） ===")
for dept, n in all_depts.most_common(5):
    print(f"  {n:>4} 人  {dept}")

print("\n=== 114 學年入學方式分布 ===")
for kind, n in summary["114"]["by_entry"].most_common():
    print(f"  {n:>4} 人  {kind}")


# ── 5.19 + 5.5 + 5.2 沙箱產生報告、5.21 存快照 ─────────
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)

    # 5.21 pickle 保存整個 summary 結構為二進位快照，方便日後重用
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:
        pickle.dump(summary, f)
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 5.5 'x' 模式：只會在檔案不存在時建立，避免不小心覆蓋舊檔
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:
        print("# 6 屆新生概況報告\n", file=f)
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)
        for year in sorted(summary):
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(
                f"| {year} | {summary[year]['total']} | "
                f"{top_dept} ({top_n}) |",
                file=f,
            )

    # 重新讀取報告內容，確認 Markdown 寫入成功
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # 驗證 pickle 是否能正確讀回原本的 summary 結構
    with open(snap, "rb") as f:
        loaded = pickle.load(f)
    print("pickle 讀回 key:", sorted(loaded.keys()))

# 離開 with → tmp 自動清掉，不在專案留任何檔案
print("\n(沙箱已自動清理)")


# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把報告改寫到 HERE / 'report.md'（改用 'w' 模式會覆蓋，'x' 會報錯）。
# 2) 加一欄「女性比例」：找出性別欄位後用 Counter 統計。
# 3) 把 summary 壓縮存成 summary.pkl.gz（gzip.open('wb') + pickle.dump）。
# 4) 跨屆找出「人數逐年下降最明顯」的系所（需要把 by_dept 按年排成折線）。
