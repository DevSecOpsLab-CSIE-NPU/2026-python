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
# HERE：目前這支 .py 檔所在資料夾（絕對路徑）
HERE = Path(__file__).resolve().parent
# 透過 parent 連續往上回到專案根，再組到 assets 壓縮檔位置
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
# assert 用於「先決條件檢查」：找不到檔案就立刻中止，錯誤訊息清楚。
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


# ── 5.7 + 5.6 + 5.1 不解壓讀 zip 裡的 CSV ──────────────
def iter_year_csv(zip_path: Path):
    """逐年 yield (年度, header, rows)。"""
    with zipfile.ZipFile(zip_path) as z:
        # infolist() 取得壓縮檔中每個成員的資訊（檔名、大小等）
        for info in z.infolist():
            # 舊 zip 的中文檔名常見 cp437 錯碼，這裡已是乾淨 utf-8
            name = info.filename
            if not name.endswith(".csv"):
                continue
            year = name[:3]  # 例如 '109_students.csv' 取前三碼當學年

            raw = z.read(info)                       # 讀出 bytes（不落地解壓）
            # utf-8-sig 可自動吃掉 BOM（Excel 匯出的 UTF-8 常見）
            text = raw.decode("utf-8-sig")           # 5.1 去 BOM
            # csv.reader 需要 file-like，StringIO 可把字串包成「像檔案」的物件
            reader = csv.reader(io.StringIO(text))   # 5.6 StringIO 當檔
            rows = list(reader)
            # yield 讓外層逐年處理，避免把所有年度邏輯塞在函式內
            yield year, rows[0], rows[1:]


# ── 跨屆統計 ───────────────────────────────────────────
summary = {}        # {年度: {'total': n, 'by_dept': Counter, 'by_entry': Counter}}
all_depts = Counter()

for year, header, rows in iter_year_csv(ZIP_PATH):
    # 先定位欄位索引，後面存取 row 才不依賴欄位順序硬編碼
    dept_idx  = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    # len(r) > idx：防禦性檢查，避免遇到缺欄位資料時 IndexError
    by_dept  = Counter(r[dept_idx]  for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    summary[year] = {
        "total":    len(rows),
        "by_dept":  by_dept,
        "by_entry": by_entry,
    }
    all_depts.update(by_dept)

# ── 終端輸出：總覽 ─────────────────────────────────────
print("\n=== 6 屆新生人數 ===")
for year in sorted(summary):
    # :>4 代表右對齊寬度 4，讓欄位看起來整齊
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

    # 5.21 pickle 保存整個 summary，日後可直接 load
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:
        pickle.dump(summary, f)
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 5.5 'x' 模式確保 Markdown 報告不被覆蓋
    report = tmp / "report.md"
    # 用 print(file=f) 可以快速產生純文字/Markdown 報表
    with open(report, "x", encoding="utf-8") as f:      # 5.5
        print("# 6 屆新生概況報告\n", file=f)           # 5.2
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)
        for year in sorted(summary):
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(f"| {year} | {summary[year]['total']} | "
                  f"{top_dept} ({top_n}) |", file=f)

    # 把 Markdown 讀回印出來（5.1 文字讀檔）
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # 驗證 pickle 讀得回來（可確認檔案沒有毀損，且資料結構正確）
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
