# =================================================================
# R01. CSV 基礎讀寫（Python 3 標準函式庫 6.1 節）
# =================================================================
# 本範例展示如何使用 Python 內建的 csv 模組來處理逗點分隔值 (CSV) 檔案。
# CSV 是一種常見的資料交換格式，廣泛應用於 Excel 與資料庫之間。

import csv
import io

# ── 範例資料：模擬一個從檔案讀入的 CSV 字串 ────────────────────────────
# 包含股票代碼、價格、日期、時間、漲跌幅、成交量
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# -----------------------------------------------------------------
# 1. csv.reader：逐列讀取，每列是一個清單 (List)
# -----------------------------------------------------------------
# 適合當你只需要簡單遍歷資料，或資料沒有明確標頭時使用。
print("=== 方法一：使用 csv.reader (結果為 List) ===")
f = io.StringIO(raw)            # 使用 io.StringIO 將字串模擬成檔案物件
reader = csv.reader(f)
headers = next(reader)          # next() 會讀取並回傳第一列（通常是欄位名稱）
print(f"解析出的標頭：{headers}")

for row in reader:
    # 這裡的 row 是一個 list，例如 ['AA', '39.48', ...]
    print(f"資料列：{row}")


# -----------------------------------------------------------------
# 2. csv.DictReader：每列自動對應成字典 (Dictionary)
# -----------------------------------------------------------------
# 最推薦的方法！它會自動將第一列作為 Key，讓你可以用名稱存取資料。
# 這樣程式碼會更具可讀性（例如 row['Price'] 比 row[1] 清楚）。
print("\n=== 方法二：使用 csv.DictReader (結果為 Dict) ===")
f = io.StringIO(raw)
for row in csv.DictReader(f):
    # row 是一個 dict，可以用欄位名稱來存取
    symbol = row['Symbol']
    price = row['Price']
    change = row['Change']
    print(f"股票：{symbol:5s} | 價格：{price:>6s} | 漲跌：{change}")


# -----------------------------------------------------------------
# 3. csv.writer：寫出 CSV 資料
# -----------------------------------------------------------------
# 將資料清單轉化為 CSV 格式的字串或存入檔案。
print("\n=== 方法三：使用 csv.writer 寫出資料 ===")
output = io.StringIO()
writer = csv.writer(output)
# 寫入標頭
writer.writerow(["Symbol", "Price", "Change"])
# 寫入多列資料
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])
print("產生的 CSV 內容：")
print(output.getvalue())


# -----------------------------------------------------------------
# 4. csv.DictWriter：以字典格式寫出 CSV
# -----------------------------------------------------------------
# 寫入時直接傳入字典，同樣能增加程式碼的維護性。
print("=== 方法四：使用 csv.DictWriter 寫出資料 ===")
output = io.StringIO()
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)

writer.writeheader()  # 必須手動呼叫來寫入標頭列
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
print("產生的 CSV 內容：")
print(output.getvalue())


# -----------------------------------------------------------------
# 提示與常用參數 (Tips)
# -----------------------------------------------------------------
# - delimiter='\t'   : 改用 Tab 分隔 (變成 TSV 檔)
# - quotechar='"'    : 指定用來包圍特殊字元的引號（預設就是雙引號）
# - quoting=csv.QUOTE_ALL : 強制讓所有欄位都被引號包起來，避免資料內含逗點導致解析錯誤。
