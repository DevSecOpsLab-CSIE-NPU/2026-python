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

# 匯入 csv 模組，用來讀取 CSV 格式資料
import csv

# 匯入 io 模組，這裡會使用 StringIO，把字串包裝成像檔案一樣可讀的物件
import io

# 匯入 pickle 模組，用來把 Python 物件儲存成二進位快照檔
import pickle

# 匯入 tempfile 模組，用來建立暫存資料夾，程式結束後可以自動清除
import tempfile

# 匯入 zipfile 模組，用來直接讀取 zip 壓縮檔內的資料，不需要手動解壓縮
import zipfile

# 從 collections 匯入 Counter
# Counter 可以很方便地統計每個項目出現的次數
from collections import Counter

# 從 pathlib 匯入 Path
# Path 可以用物件導向的方式處理路徑，比傳統字串路徑更清楚
from pathlib import Path

# ── 5.11 / 5.12 找到資料檔 ─────────────────────────────

# __file__ 代表目前這個 Python 程式檔案的位置
# resolve() 會轉成絕對路徑
# parent 代表取得目前程式所在的資料夾
HERE = Path(__file__).resolve().parent

# 組出 zip 資料檔的位置
# HERE.parent.parent.parent 代表往上三層資料夾
# 再進入 assets 資料夾，找到 npu-stu-109-114-anon.zip
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"

# 檢查 ZIP_PATH 指向的檔案是否真的存在
# 如果不存在，程式會停止，並印出找不到資料的錯誤訊息
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"

# 印出資料來源的檔名，讓使用者知道目前讀取的是哪一個 zip 檔
print("資料來源:", ZIP_PATH.name)


# ── 5.7 + 5.6 + 5.1 不解壓讀 zip 裡的 CSV ──────────────

# 定義一個函式 iter_year_csv
# 功能：逐一讀取 zip 檔裡面的 CSV 檔案
# 每讀到一個 CSV，就回傳該年度、欄位標題 header、以及資料列 rows
def iter_year_csv(zip_path: Path):
    """逐年 yield (年度, header, rows)。"""

    # 使用 zipfile.ZipFile 開啟 zip 壓縮檔
    # with 的好處是離開區塊後會自動關閉檔案
    with zipfile.ZipFile(zip_path) as z:

        # z.infolist() 會列出 zip 檔內所有檔案的資訊
        # 每一個 info 代表 zip 裡面的一個檔案或資料項目
        for info in z.infolist():

            # 取得 zip 內部檔案的檔名
            # 例如可能是 109.csv、110.csv 等
            # 舊 zip 的中文檔名常見 cp437 錯碼，這裡已是乾淨 utf-8
            name = info.filename

            # 如果檔名不是以 .csv 結尾，就跳過不處理
            # 這樣可以避免讀到 zip 裡面其他非 CSV 檔案
            if not name.endswith(".csv"):
                continue

            # 取檔名前 3 個字元作為學年度
            # 例如 109.csv 的前 3 個字元就是 109
            year = name[:3]  # '109'~'114'

            # 從 zip 裡直接讀取該 CSV 檔案內容
            # z.read(info) 讀出來的是 bytes，也就是二進位資料
            raw = z.read(info)                       # bytes

            # 將 bytes 解碼成文字
            # utf-8-sig 可以處理 Excel 產生 CSV 時可能出現的 BOM
            # 如果不用 utf-8-sig，有時第一個欄位名稱前面會多出奇怪符號
            text = raw.decode("utf-8-sig")           # 5.1 去 BOM

            # csv.reader 需要讀取「像檔案一樣」的物件
            # io.StringIO(text) 可以把文字字串包成 file-like object
            reader = csv.reader(io.StringIO(text))   # 5.6 StringIO 當檔

            # 將 reader 讀到的所有資料轉成 list
            # rows[0] 會是第一列，也就是欄位名稱
            # rows[1:] 則是從第二列開始的學生資料
            rows = list(reader)

            # yield 會一次回傳一個年度的資料
            # rows[0] 是 header 欄位名稱
            # rows[1:] 是實際資料內容
            yield year, rows[0], rows[1:]


# ── 跨屆統計 ───────────────────────────────────────────

# 建立 summary 字典，用來保存每個學年度的統計結果
# 格式：
# {
#   '109': {
#       'total': 總人數,
#       'by_dept': 各系所人數統計,
#       'by_entry': 各入學方式人數統計
#   },
#   ...
# }
summary = {}        # {年度: {'total': n, 'by_dept': Counter, 'by_entry': Counter}}

# 建立 all_depts，用來統計 109~114 六屆所有系所的累計人數
all_depts = Counter()

# 呼叫 iter_year_csv(ZIP_PATH)，逐年取得 zip 裡每個 CSV 的資料
# year 是學年度
# header 是欄位名稱
# rows 是該年度所有學生資料
for year, header, rows in iter_year_csv(ZIP_PATH):

    # 找出「系所名稱」這個欄位在 CSV 裡的位置
    # 之後就可以用這個索引值去每一列資料中取出系所名稱
    dept_idx  = header.index("系所名稱")

    # 找出「入學方式」這個欄位在 CSV 裡的位置
    # 之後就可以用這個索引值去每一列資料中取出入學方式
    entry_idx = header.index("入學方式")

    # 統計該年度每個系所的人數
    # r[dept_idx] 代表某一列學生資料中的系所名稱
    # if len(r) > dept_idx 是為了避免資料列欄位不足造成索引錯誤
    by_dept  = Counter(r[dept_idx]  for r in rows if len(r) > dept_idx)

    # 統計該年度每種入學方式的人數
    # r[entry_idx] 代表某一列學生資料中的入學方式
    # if len(r) > entry_idx 一樣是避免資料列欄位不足造成錯誤
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    # 將該年度的統計資料存入 summary 字典
    # total 存該年度總筆數
    # by_dept 存各系所人數統計
    # by_entry 存各入學方式人數統計
    summary[year] = {
        "total":    len(rows),
        "by_dept":  by_dept,
        "by_entry": by_entry,
    }

    # 將該年度的系所統計加到 all_depts 裡
    # update 可以把 Counter 的統計數量累加進去
    # 最後 all_depts 會變成六屆累計的各系所人數
    all_depts.update(by_dept)

# ── 終端輸出：總覽 ─────────────────────────────────────

# 印出標題，表示接下來要顯示六屆新生總人數
print("\n=== 6 屆新生人數 ===")

# 依照學年度排序後逐一印出各年度總人數
for year in sorted(summary):

    # summary[year]['total'] 是該年度總人數
    # :>4 表示輸出時靠右對齊，寬度至少 4 格，讓畫面比較整齊
    print(f"  {year} 學年：{summary[year]['total']:>4} 人")

# 印出標題，表示接下來要顯示六屆累計最熱門的前五個系所
print("\n=== 全體最熱門 5 個系所（累計 6 屆） ===")

# most_common(5) 會取出 Counter 中數量最多的前 5 筆
# dept 是系所名稱，n 是累計人數
for dept, n in all_depts.most_common(5):

    # 印出該系所六屆累計人數
    # :>4 一樣是為了讓數字靠右對齊
    print(f"  {n:>4} 人  {dept}")

# 印出標題，表示接下來要顯示 114 學年的入學方式分布
print("\n=== 114 學年入學方式分布 ===")

# 取出 summary 中 114 學年的 by_entry 統計結果
# most_common() 不放數字代表全部列出，並按照人數由多到少排序
for kind, n in summary["114"]["by_entry"].most_common():

    # kind 是入學方式，n 是該入學方式的人數
    print(f"  {n:>4} 人  {kind}")


# ── 5.19 + 5.5 + 5.2 沙箱產生報告、5.21 存快照 ─────────

# 建立一個暫存資料夾
# with tempfile.TemporaryDirectory() as tmp:
# 會在 with 區塊內建立暫存資料夾
# 離開 with 區塊後，這個暫存資料夾會自動刪除
with tempfile.TemporaryDirectory() as tmp:

    # 將 tmp 轉成 Path 物件
    # 這樣後面可以用 tmp / "檔名" 的方式組路徑
    tmp = Path(tmp)

    # 5.21 pickle 保存整個 summary，日後可直接 load

    # 設定 pickle 快照檔案的位置
    # 這個檔案會建立在暫存資料夾中
    snap = tmp / "summary.pkl"

    # 以二進位寫入模式開啟 summary.pkl
    # "wb" 代表 write binary
    with open(snap, "wb") as f:

        # 使用 pickle.dump 將 summary 物件寫入檔案
        # 這樣之後可以不用重新統計，直接讀取統計結果
        pickle.dump(summary, f)

    # 印出快照檔案名稱與檔案大小
    # snap.stat().st_size 可以取得檔案大小，單位是 bytes
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 5.5 'x' 模式確保 Markdown 報告不被覆蓋

    # 設定 Markdown 報告檔案的位置
    report = tmp / "report.md"

    # 使用 "x" 模式建立檔案
    # "x" 代表 exclusive creation
    # 如果檔案已存在，就會報錯，避免不小心覆蓋舊報告
    with open(report, "x", encoding="utf-8") as f:      # 5.5

        # 將 Markdown 標題寫入 report.md
        # print(..., file=f) 代表把內容輸出到檔案，而不是螢幕
        print("# 6 屆新生概況報告\n", file=f)           # 5.2

        # 寫入 Markdown 表格的欄位名稱
        print("| 學年 | 人數 | 第一大系所 |", file=f)

        # 寫入 Markdown 表格的分隔線
        print("|------|------|------------|", file=f)

        # 依照學年度排序，逐年寫入表格內容
        for year in sorted(summary):

            # 取得該年度人數最多的系所
            # most_common(1)[0] 代表取出排名第一的項目
            # top_dept 是第一大系所名稱
            # top_n 是該系所人數
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]

            # 寫入 Markdown 表格的一列
            # 內容包含：學年度、總人數、第一大系所與該系所人數
            print(f"| {year} | {summary[year]['total']} | "
                  f"{top_dept} ({top_n}) |", file=f)

    # 把 Markdown 讀回印出來（5.1 文字讀檔）

    # 印出標題，表示接下來要預覽剛剛產生的 Markdown 報告
    print("\n=== Markdown 報告預覽 ===")

    # 使用 read_text 讀取 report.md 內容
    # encoding="utf-8" 表示用 UTF-8 編碼讀取，避免中文亂碼
    print(report.read_text(encoding="utf-8"))

    # 驗證 pickle 讀得回來（型別、內容一致）

    # 以二進位讀取模式開啟剛剛寫入的 summary.pkl
    # "rb" 代表 read binary
    with open(snap, "rb") as f:

        # 使用 pickle.load 把檔案中的資料讀回 Python 物件
        loaded = pickle.load(f)

    # 印出讀回來的資料有哪些學年度 key
    # 如果能正確印出 109~114，代表 pickle 儲存與讀取成功
    print("pickle 讀回 key:", sorted(loaded.keys()))

# 離開 with → tmp 自動清掉，不在專案留任何檔案

# 這行會在離開 TemporaryDirectory 的 with 區塊後執行
# 此時暫存資料夾已經自動刪除
print("\n(沙箱已自動清理)")


# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把報告改寫到 HERE / 'report.md'（改用 'w' 模式會覆蓋，'x' 會報錯）。
# 2) 加一欄「女性比例」：找出性別欄位後用 Counter 統計。
# 3) 把 summary 壓縮存成 summary.pkl.gz（gzip.open('wb') + pickle.dump）。
# 4) 跨屆找出「人數逐年下降最明顯」的系所（需要把 by_dept 按年排成折線）。