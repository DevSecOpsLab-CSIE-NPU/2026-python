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

# ── 5.11 / 5.12 找到資料檔 ─────────────────────────────
# 這裡透過 pathlib 先定位本程式所在資料夾，再往上找到 assets 資料夾中的 zip 檔
# Path(__file__).resolve().parent 取得此程式的絕對資料夾路徑
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


# ── 5.7 + 5.6 + 5.1 不解壓讀 zip 裡的 CSV ──────────────
def iter_year_csv(zip_path: Path):
    """逐年 yield (年度, header, rows)。"""
    with zipfile.ZipFile(zip_path) as z:
        # ZipFile 物件可以讀取壓縮檔內的每個成員資訊
        for info in z.infolist():
            # 舊 zip 的中文檔名常見 cp437 錯碼，這裡假定檔名已是乾淨的 utf-8
            name = info.filename
            if not name.endswith(".csv"):
                # 跳過非 CSV 檔案，例如 __MACOSX 子資料夾或其他檔案
                continue
            # 取檔名前三個字作為學年度，例如 '109'~'114'
            year = name[:3]

            # 直接從 zip 內讀出 bytes，不解壓到硬碟
            raw = z.read(info)
            # utf-8-sig 能自動移除 BOM，適合處理 Excel 另存為的 CSV
            text = raw.decode("utf-8-sig")
            # StringIO 讓文字字串變成像檔案一樣的物件
            reader = csv.reader(io.StringIO(text))
            rows = list(reader)
            # 回傳學年度、標題列，以及後面的資料列
            yield year, rows[0], rows[1:]


# ── 跨屆統計 ───────────────────────────────────────────
# summary 會存放每一年度的統計結果
summary = {}        # {年度: {'total': n, 'by_dept': Counter, 'by_entry': Counter}}
# all_depts 用來累計所有年度的系所人數
all_depts = Counter()

for year, header, rows in iter_year_csv(ZIP_PATH):
    # 先找出欄位在標題列中的位置
    dept_idx  = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    # 只對包含該欄位的列進行統計，避免資料列長度不足時出錯
    by_dept  = Counter(r[dept_idx]  for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    summary[year] = {
        "total":    len(rows),
        "by_dept":  by_dept,
        "by_entry": by_entry,
    }
    # 更新全年度系所累積計數
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
# 使用 TemporaryDirectory 建立臨時資料夾，離開後會自動清理，不會殘留測試檔案
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)

    # 5.21 pickle 保存整個 summary 為二進位快照
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:
        pickle.dump(summary, f)
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 5.5 'x' 模式寫 report.md，若檔案已存在會直接失敗，確保不覆蓋原檔
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:
        print("# 6 屆新生概況報告\n", file=f)
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)
        for year in sorted(summary):
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(f"| {year} | {summary[year]['total']} | "
                  f"{top_dept} ({top_n}) |", file=f)

    # 5.1 以 UTF-8 讀回 Markdown 檔案內容並印出預覽
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # 驗證 pickle 讀取是否正常，讀回後 key 應與 summary 相同
    with open(snap, "rb") as f:
        loaded = pickle.load(f)
    print("pickle 讀回 key:", sorted(loaded.keys()))

# 離開 with 後，TemporaryDirectory 建立的檔案與資料夾會自動刪除
print("\n(沙箱已自動清理)")


# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把報告改寫到 HERE / 'report.md'（改用 'w' 模式會覆蓋，'x' 會報錯）。
# 2) 加一欄「女性比例」：找出性別欄位後用 Counter 統計。
# 3) 把 summary 壓縮存成 summary.pkl.gz（gzip.open('wb') + pickle.dump）。
# 4) 跨屆找出「人數逐年下降最明顯」的系所（需要把 by_dept 按年排成折線）。
