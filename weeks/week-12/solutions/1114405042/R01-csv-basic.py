"""
R01. CSV 基礎讀寫（6.1）

本模組展示 Python 內建 csv 模組的四種主要用法：
    1. csv.reader - 逐列讀取 CSV，每列返回 list
    2. csv.DictReader - 逐列讀取 CSV，每列返回 dict（自動對應欄位名）
    3. csv.writer - 將資料逐列寫入 CSV（接收 list）
    4. csv.DictWriter - 將資料逐列寫入 CSV（接收 dict）

csv 模組特別適合處理含有逗號、引號等特殊字元的 CSV 格式資料。
"""

import csv  # Python 內建的 CSV 讀寫模組
import io   # 用來在記憶體中模擬檔案操作（StringIO）

# ── 範例資料（模擬 CSV 字串）────────────────────────────
# 這是一個模擬的 CSV 格式字串，包含股票行情資訊：
# - 第一列：欄位標頭（Symbol, Price, Date, Time, Change, Volume）
# - 後續列：各股票的具體資料
# 使用原始字串（三引號）保留換行符，使資料格式保持完整
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列是 list ───────────────
# csv.reader 是最基礎的讀取方式，它：
# 1. 將 CSV 檔案逐列解析
# 2. 每一列返回一個 list（包含該列的所有欄位）
# 3. 需要手動處理標頭與資料的分離
# 
# io.StringIO() 用來在記憶體中模擬一個檔案對象（這裡模擬讀取 raw 字串）
# next(reader) 表示讀取迭代器的下一個值（即讀取第一列）
print("=== csv.reader ===")
f = io.StringIO(raw)  # 將字串包裝成像檔案一樣可以逐行讀取
reader = csv.reader(f)  # 建立 CSV 讀取器
headers = next(reader)  # 使用 next() 讀取第一列當作標頭
print("標頭：", headers)  # 輸出標頭列表
for row in reader:  # 遍歷剩餘的所有列
    print(row)  # 每 row 是一個 list，例如 ['AA', '39.48', '6/11/2007', ...]

# ── 6.1 csv.DictReader：每列自動對應成 dict ──────────────
# csv.DictReader 是更方便的讀取方式，它：
# 1. 自動讀取第一列作為欄位名稱
# 2. 將每一列轉換為 dict，鍵為欄位名稱，值為該欄位的資料
# 3. 可以用欄位名直接訪問資料，而無需記住欄位順序
#
# 優勢：程式碼更清晰易讀，且不易出錯（透過欄位名訪問而非索引）
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
for row in csv.DictReader(f):  # 每個 row 都是一個 dict
    # 透過欄位名直接訪問資料，例如 row['Symbol']、row['Price'] 等
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV ─────────────────────────────
# csv.writer 用於將資料寫入 CSV 格式，它：
# 1. 接收 list 作為每一列的資料
# 2. 自動處理特殊字元的轉義（例如含逗號或引號的資料）
# 3. 逐列寫入資料，每次 writerow() 寫一列
#
# 在這個例子中，我們使用 StringIO 在記憶體中模擬寫入過程，
# 然後透過 getvalue() 取得寫入的結果
print("\n=== csv.writer ===")
output = io.StringIO()  # 建立一個記憶體中的檔案
writer = csv.writer(output)  # 建立 CSV 寫入器
writer.writerow(["Symbol", "Price", "Change"])  # 寫入標頭列
writer.writerow(["AA", 39.48, -0.18])  # 寫入第一筆資料
writer.writerow(["AIG", 71.38, -0.15])  # 寫入第二筆資料
print(output.getvalue())  # 輸出寫入的結果

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV ─────────────────
# csv.DictWriter 是用字典進行寫入的方式，它：
# 1. 需要預先定義欄位名稱列表（fieldnames）
# 2. writeheader() 方法寫入標頭列
# 3. writerow() 接收 dict，按照 fieldnames 的順序寫入欄位值
#
# 優勢：與 DictReader 搭配使用時，程式碼更加一致和易讀
print("=== csv.DictWriter ===")
output = io.StringIO()
fieldnames = ["Symbol", "Price", "Change"]  # 定義欄位名稱和順序
writer = csv.DictWriter(output, fieldnames=fieldnames)  # 建立 DictWriter
writer.writeheader()  # 寫入標頭列
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})  # 寫入資料為 dict 格式
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})  # 鍵必須與 fieldnames 對應
print(output.getvalue())

# ── 常用參數 ─────────────────────────────────────────────
# csv.reader() 和 csv.writer() 都支持以下常用參數：
#
# delimiter（分隔符）：
#   - 默認值：','（逗號）
#   - delimiter='\t' 表示使用 Tab 作為分隔符，適合 TSV（Tab-Separated Values）檔案
#
# quotechar（引號字元）：
#   - 默認值：'"'（雙引號）
#   - 用於包圍含有特殊字元的欄位，例如含逗號的資料
#
# quoting（引號策略）：
#   - csv.QUOTE_MINIMAL：只在必要時加引號（默認）
#   - csv.QUOTE_ALL：每個欄位都加引號
#   - csv.QUOTE_NONNUMERIC：非數字欄位加引號
#   - csv.QUOTE_NONE：不使用引號（需指定 escapechar）
#
# 例如：
#   writer = csv.writer(f, delimiter='\t')  # 使用 Tab 分隔的 TSV 檔案
#   writer = csv.writer(f, quoting=csv.QUOTE_ALL)  # 所有欄位都加引號
#   writer = csv.writer(f, delimiter=';', quotechar="'")  # 分號分隔，單引號作為引號字元
