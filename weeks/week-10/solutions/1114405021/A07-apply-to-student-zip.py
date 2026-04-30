# A07. 綜合應用：把 I/O 技巧套到真實學生資料
# Bloom: Apply — 這支程式的目的不是單一 API 示範，
# 而是把前面學過的路徑、壓縮檔、CSV、暫存目錄、報告輸出等技巧，
# 串成一條完整的資料處理流程。
#
# 資料來源：assets/npu-stu-109-114-anon.zip
# 這是一包匿名化後的 6 屆新生資料，每一個年度通常對應一個 CSV 檔。
#
# 用到的小節對照：
#   5.11 pathlib：先把目前檔案所在位置算出來，再組出資料檔路徑
#   5.12 exists：在讀檔前先確認 zip 是否真的存在，避免後面才爆錯
#   5.7  zipfile：直接讀壓縮檔內的內容，不需要先人工解壓
#   5.1  encoding='utf-8-sig'：處理 Excel / 匯出工具常帶的 BOM
#   5.6  io.StringIO：把解碼後的字串包成類檔案物件，方便 csv.reader 使用
#   5.19 TemporaryDirectory：把輸出結果放進沙箱，結束後自動清掉
#   5.5  open(..., 'x')：只在檔案不存在時建立，避免覆蓋到既有報告
#   5.21 pickle：把統計結果存成快照，之後可快速還原
#   5.2  print(file=)：直接把 Markdown 內容寫進報告檔

import csv
import io
import pickle
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

# ── 5.11 / 5.12 找到資料檔 ─────────────────────────────
# 先以目前這支程式的位置為基準，往上回推到專案根目錄，
# 再拼出 assets 底下的 zip 檔路徑。
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


# ── 5.7 + 5.6 + 5.1 不解壓讀 zip 裡的 CSV ──────────────
# 這個函式負責把 zip 檔中的每一年 CSV 逐一讀出來。
# 流程是：zip bytes -> UTF-8 解碼 -> StringIO -> csv.reader -> rows。
# 這樣可以直接在記憶體中處理資料，不需要把壓縮檔展開到磁碟。
def iter_year_csv(zip_path: Path):
    """逐年 yield (年度, header, rows)。

    回傳格式說明：
    - year：年度字串，例如 '109'
    - header：CSV 第一列欄位名稱
    - rows：不含表頭的資料列清單
    """
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            # 逐個檔案檢查，只保留副檔名為 .csv 的成員。
            # 這裡假設檔名像 109.csv、110.csv ...，前 3 碼就是學年度。
            name = info.filename
            if not name.endswith(".csv"):
                continue
            year = name[:3]  # '109'~'114'

            # 先以 bytes 讀出壓縮內容，再轉成文字。
            # utf-8-sig 會自動忽略 BOM，避免第一個欄位名稱前面多出隱藏字元。
            raw = z.read(info)
            text = raw.decode("utf-8-sig")

            # csv.reader 需要的是「像檔案一樣」的物件，StringIO 正好能把字串包起來。
            reader = csv.reader(io.StringIO(text))
            rows = list(reader)
            yield year, rows[0], rows[1:]


# ── 跨屆統計 ───────────────────────────────────────────
# summary 用來保存每個年度的統計結果：
# total    -> 該年度總筆數
# by_dept  -> 依系所名稱統計人數
# by_entry -> 依入學方式統計人數
summary = {}
all_depts = Counter()

for year, header, rows in iter_year_csv(ZIP_PATH):
    # 先找到欄位在表頭中的位置，之後才能從每一列資料中取出對應欄位。
    # 這樣即使 CSV 欄位順序改動，只要欄名還在，程式仍然能正常運作。
    dept_idx  = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    # Counter 會自動統計每個值出現幾次，適合拿來做分布分析。
    by_dept  = Counter(r[dept_idx]  for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    # 將每一年的統計結果整理成固定格式，方便後面輸出與存檔。
    summary[year] = {
        "total":    len(rows),
        "by_dept":  by_dept,
        "by_entry": by_entry,
    }
    # all_depts 用來累積跨年度的系所總分布，最後可以找出最熱門的系所。
    all_depts.update(by_dept)

# ── 終端輸出：總覽 ─────────────────────────────────────
# 這三段輸出是給人直接在終端機閱讀的摘要資訊：
# 1. 每年總人數
# 2. 六屆合併後最熱門系所
# 3. 114 學年的入學方式分布
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
# TemporaryDirectory 會建立一個暫時資料夾，with 結束時自動刪除。
# 這裡把 pickle 快照和 Markdown 報告都先寫進沙箱，避免污染專案目錄。
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)

    # pickle 會把 Python 物件序列化成二進位檔，適合快速保存統計結果。
    # 這裡存的是整個 summary，因此未來若要重跑分析，可以直接讀回來用。
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:
        pickle.dump(summary, f)
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 'x' 模式表示「只有在檔案不存在時才建立」：
    # 如果同名檔案已存在，open 會直接報錯，避免不小心覆蓋報告內容。
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:
        # 用 print(..., file=f) 直接把 Markdown 寫入檔案，
        # 這種寫法對表格與標題很方便，閱讀上也很直覺。
        print("# 6 屆新生概況報告\n", file=f)
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)
        for year in sorted(summary):
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(f"| {year} | {summary[year]['total']} | "
                  f"{top_dept} ({top_n}) |", file=f)

    # 產生完報告後，再把內容讀回來印到終端，方便立即檢查格式是否正確。
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # 再把 pickle 讀回來，確認序列化與反序列化都正常，
    # 這一步也順便證明 summary 的結構可以被完整保存與還原。
    with open(snap, "rb") as f:
        loaded = pickle.load(f)
    print("pickle 讀回 key:", sorted(loaded.keys()))

# 離開 with 區塊後，TemporaryDirectory 會自動刪除暫存資料夾，
# 因此整個流程不會在專案目錄留下中間檔。
print("\n(沙箱已自動清理)")


# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把報告改寫到 HERE / 'report.md'（改用 'w' 模式會覆蓋，'x' 會報錯）。
# 2) 加一欄「女性比例」：找出性別欄位後用 Counter 統計。
# 3) 把 summary 壓縮存成 summary.pkl.gz（gzip.open('wb') + pickle.dump）。
# 4) 跨屆找出「人數逐年下降最明顯」的系所（需要把 by_dept 按年排成折線）。
