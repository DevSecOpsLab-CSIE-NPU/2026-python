# A07. 綜合應用：把 I/O 技巧套到真實學生資料
# 這份版本保留原本的功能，但補上較完整的繁體中文註解，方便課後複習。
#
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
# HERE 代表目前這支腳本所在的資料夾。
# 之後用相對路徑往上推回專案根目錄，再定位到 assets 底下的 zip 檔。
HERE = Path(__file__).resolve().parent


def _find_zip_path() -> Path:
    """從目前檔案位置往上找，直到找到 assets 底下的資料壓縮檔。"""
    for base in [HERE, *HERE.parents]:
        candidate = base / "assets" / "npu-stu-109-114-anon.zip"
        if candidate.exists():
            return candidate
    raise FileNotFoundError("找不到 assets/npu-stu-109-114-anon.zip")


ZIP_PATH = _find_zip_path()

# 如果資料檔不存在，立刻報錯，避免後面讀檔才發現問題。
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


# ── 5.7 + 5.6 + 5.1 不解壓讀 zip 裡的 CSV ──────────────
def iter_year_csv(zip_path: Path):
    """逐年 yield (年度, header, rows)。

    這個函式會把 zip 內每個年度的 CSV 檔讀出來，
    但不會真的解壓到硬碟，這樣可以減少暫存檔管理成本。
    """
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            # 舊 zip 的中文檔名常見 cp437 錯碼，這裡已是乾淨 utf-8
            name = info.filename
            if not name.endswith(".csv"):
                continue

            # 檔名前 3 碼就是學年，例如 109、110、111 ... 114
            year = name[:3]

            # ZipFile.read() 讀出來的是 bytes，所以要先解碼成文字。
            raw = z.read(info)
            text = raw.decode("utf-8-sig")

            # csv.reader 需要可逐行讀取的文字檔物件，StringIO 可直接模擬。
            reader = csv.reader(io.StringIO(text))
            rows = list(reader)
            yield year, rows[0], rows[1:]


# ── 跨屆統計 ───────────────────────────────────────────
# summary 會存每個年度的統計結果。
# 結構大致如下：
# {
#   '109': {'total': n, 'by_dept': Counter(...), 'by_entry': Counter(...)},
#   ...
# }
summary = {}

# all_depts 用來彙整 6 屆的系所總人數，方便找出熱門系所。
all_depts = Counter()

for year, header, rows in iter_year_csv(ZIP_PATH):
    # 先找出關鍵欄位在表頭中的位置，之後就能用索引直接讀每筆資料。
    dept_idx = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    # Counter 很適合拿來做分類統計。
    # 這裡分別統計每個系所、每種入學方式的次數。
    by_dept = Counter(r[dept_idx] for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    summary[year] = {
        "total": len(rows),
        "by_dept": by_dept,
        "by_entry": by_entry,
    }
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
# TemporaryDirectory 會在離開區塊後自動清空，適合做測試輸出。
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)

    # 5.21 pickle 可把 Python 物件整包序列化，日後可直接還原。
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:
        pickle.dump(summary, f)
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 5.5 使用 'x' 模式，表示檔案已存在就報錯，避免覆蓋原始結果。
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:
        # 5.2 print(file=...) 可以直接把文字寫進 Markdown 檔。
        print("# 6 屆新生概況報告\n", file=f)
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)
        for year in sorted(summary):
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(
                f"| {year} | {summary[year]['total']} | {top_dept} ({top_n}) |",
                file=f,
            )

    # 把 Markdown 讀回來，直接印在終端機上，方便快速檢查內容。
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # 驗證 pickle 可以正常讀回，確認序列化與反序列化都沒問題。
    with open(snap, "rb") as f:
        loaded = pickle.load(f)
    print("pickle 讀回 key:", sorted(loaded.keys()))

# 離開 with 區塊後，tmp 目錄會自動刪除，不會在專案中留下暫存檔。
print("\n(沙箱已自動清理)")


# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把報告改寫到 HERE / 'report.md'（改用 'w' 模式會覆蓋，'x' 會報錯）。
# 2) 加一欄「女性比例」：找出性別欄位後用 Counter 統計。
# 3) 把 summary 壓縮存成 summary.pkl.gz（gzip.open('wb') + pickle.dump）。
# 4) 跨屆找出「人數逐年下降最明顯」的系所（需要把 by_dept 按年排成折線）。