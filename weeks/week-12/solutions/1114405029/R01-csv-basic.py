# R01. CSV 基礎讀寫（6.1）
# csv.reader / csv.writer / csv.DictReader / csv.DictWriter

# 匯入 Python 內建的 csv 模組
# csv 模組專門用來讀取與寫入 CSV 格式資料
import csv

# 匯入 io 模組
# io.StringIO 可以把「字串」模擬成「檔案物件」
# 這樣就可以不用真的建立 .csv 檔案，也能練習 CSV 讀寫
import io

# ── 範例資料（模擬 CSV 字串）────────────────────────────
# raw 是一個多行字串，用來模擬 CSV 檔案的內容
# 第一列 Symbol,Price,Date,Time,Change,Volume 是欄位名稱，也就是表頭
# 後面每一列代表一筆股票資料
# CSV 的欄位之間使用逗號 , 分隔
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列是 list ───────────────
# 印出區塊標題，方便觀察目前示範的是 csv.reader
print("=== csv.reader ===")

# 使用 io.StringIO(raw) 將 raw 字串轉成類似檔案的物件
# 因為 csv.reader() 需要讀取的是檔案物件或類似檔案的資料
f = io.StringIO(raw)

# 建立 csv.reader 物件
# reader 會一列一列讀取 CSV
# 每讀到一列，會把該列資料轉成 list
reader = csv.reader(f)

# 使用 next(reader) 讀取第一列
# 因為第一列是欄位名稱，所以存到 headers 變數
# 讀取後，reader 會自動往下一列移動
headers = next(reader)          # 第一列當標頭

# 印出 CSV 的標頭欄位
print("標頭：", headers)

# 使用 for 迴圈讀取剩下的每一列資料
# 每一個 row 都是一個 list
for row in reader:
    # 印出每一列資料
    print(row)

# ── 6.1 csv.DictReader：每列自動對應成 dict ──────────────
# 印出區塊標題，方便觀察目前示範的是 csv.DictReader
print("\n=== csv.DictReader ===")

# 重新建立 StringIO 物件
# 因為前面的 f 已經被讀取過了，讀取位置已經在最後
# 所以這裡需要重新用 raw 建立一次新的檔案物件
f = io.StringIO(raw)

# csv.DictReader 會自動把第一列當作欄位名稱
# 後面的每一列資料會轉成 dictionary
# 例如 row['Symbol'] 可以取得 Symbol 欄位的值
for row in csv.DictReader(f):
    # 使用 f-string 格式化輸出
    # row['Symbol']:5s 代表 Symbol 欄位寬度至少 5 個字元，字串靠左
    # row['Price']:>6s 代表 Price 欄位寬度至少 6 個字元，字串靠右
    # row['Change'] 代表漲跌欄位
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV ─────────────────────────────
# 印出區塊標題，方便觀察目前示範的是 csv.writer
print("\n=== csv.writer ===")

# 建立一個空的 StringIO 物件
# output 可以暫時存放寫出的 CSV 內容
output = io.StringIO()

# 建立 csv.writer 物件
# writer 可以把 list 資料寫成 CSV 格式
writer = csv.writer(output)

# 寫入 CSV 的第一列，也就是欄位名稱
writer.writerow(["Symbol", "Price", "Change"])

# 寫入第一筆資料
# writerow() 會把 list 中的資料用逗號分隔後寫入
writer.writerow(["AA", 39.48, -0.18])

# 寫入第二筆資料
writer.writerow(["AIG", 71.38, -0.15])

# 使用 output.getvalue() 取得目前寫入到 StringIO 裡面的完整 CSV 字串
print(output.getvalue())

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV ─────────────────
# 印出區塊標題，方便觀察目前示範的是 csv.DictWriter
print("=== csv.DictWriter ===")

# 重新建立一個空的 StringIO 物件
# 用來存放 DictWriter 寫出的 CSV 內容
output = io.StringIO()

# 定義 CSV 欄位名稱
# DictWriter 會根據這個順序輸出欄位
fieldnames = ["Symbol", "Price", "Change"]

# 建立 csv.DictWriter 物件
# fieldnames 用來指定 dictionary 中哪些 key 要被寫入 CSV
writer = csv.DictWriter(output, fieldnames=fieldnames)

# 寫入 CSV 的表頭
# 也就是 Symbol,Price,Change 這一列
writer.writeheader()

# 寫入第一筆 dictionary 資料
# dictionary 的 key 必須對應到 fieldnames 裡面的欄位名稱
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})

# 寫入第二筆 dictionary 資料
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})

# 印出 DictWriter 寫出的完整 CSV 內容
print(output.getvalue())

# ── 常用參數 ─────────────────────────────────────────────
# delimiter='\t'   → TSV（Tab 分隔）
# quotechar='"'    → 引號字元
# quoting=csv.QUOTE_ALL → 每個欄位都加引號