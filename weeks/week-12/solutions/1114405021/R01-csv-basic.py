# R01. CSV 基礎讀寫（6.1）
# 這個範例示範 csv 模組最常見的四種用法：
# 1. csv.reader：把每一列讀成 list
# 2. csv.DictReader：把每一列讀成 dict
# 3. csv.writer：把資料寫成 CSV 格式
# 4. csv.DictWriter：把 dict 寫成 CSV 格式

import csv
import io

# -----------------------------------------------------------------------------
# 範例資料
# -----------------------------------------------------------------------------
# 這裡使用三引號建立一段多行字串，模擬一份 CSV 檔案的內容。
# 每一行代表一筆資料，欄位之間用逗號分隔。
# 實際專案中，這段內容通常會來自 open('file.csv') 讀到的檔案內容。
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# -----------------------------------------------------------------------------
# 1. csv.reader：逐列讀取，每一列會變成 list
# -----------------------------------------------------------------------------
# csv.reader 會把每一行拆成欄位陣列，適合你只想要「照順序」取值的情況。
# 它不會幫你理解欄位名稱，所以你要自己知道第 1 欄、第 2 欄代表什麼。
print("=== csv.reader ===")

# StringIO 可以把字串包裝成像檔案一樣的物件，讓 csv.reader 直接讀取。
f = io.StringIO(raw)
reader = csv.reader(f)

# next(reader) 會取得第一列，也就是標頭列。
# 這裡先把標頭分離出來，後面才知道欄位名稱。
headers = next(reader)
print("標頭：", headers)

# 從第二列開始逐筆讀取，每個 row 都是一個 list。
for row in reader:
    print(row)

# -----------------------------------------------------------------------------
# 2. csv.DictReader：逐列讀取，每一列會變成 dict
# -----------------------------------------------------------------------------
# DictReader 會自動把標頭列當成 key，讓每一列資料變成字典。
# 這樣你就可以用欄位名稱直接取值，不用自己記索引位置。
print("\n=== csv.DictReader ===")

f = io.StringIO(raw)
for row in csv.DictReader(f):
    # row['Symbol']、row['Price']、row['Change'] 都是字串。
    # 這裡用格式化字串把欄位對齊，方便閱讀輸出結果。
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# -----------------------------------------------------------------------------
# 3. csv.writer：把資料寫成 CSV 格式
# -----------------------------------------------------------------------------
# writer 會把你傳入的 list 轉成 CSV 格式並輸出到檔案物件。
# 這裡同樣用 StringIO 當作暫存區，方便直接印出結果。
print("\n=== csv.writer ===")
output = io.StringIO()
writer = csv.writer(output)

# writer.writerow() 會寫入一整列。
# 第一列通常是標頭，後面再依序寫入資料。
writer.writerow(["Symbol", "Price", "Change"])
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])

# getvalue() 可以把 StringIO 裡面累積的內容取出來。
print(output.getvalue())

# -----------------------------------------------------------------------------
# 4. csv.DictWriter：把 dict 寫成 CSV 格式
# -----------------------------------------------------------------------------
# DictWriter 比較適合欄位固定、且資料本來就是字典的情境。
# 你只要提供欄位順序，之後每筆資料直接丟 dict 就可以。
print("=== csv.DictWriter ===")
output = io.StringIO()
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)

# writeheader() 會依照 fieldnames 自動寫出標頭列。
writer.writeheader()

# writerow() 接受一個 dict，key 會對應到欄位名稱。
writer.writerow({"Symbol": "AA", "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})

print(output.getvalue())

# -----------------------------------------------------------------------------
# 常用參數補充
# -----------------------------------------------------------------------------
# delimiter='\t'：把分隔符號改成 Tab，可用來讀寫 TSV。
# quotechar='"'：指定包住欄位值的引號字元。
# quoting=csv.QUOTE_ALL：輸出時每個欄位都加上引號。
#
# 這些參數在欄位內容含有逗號、換行或引號時特別重要，
# 可以避免 CSV 內容被誤拆或格式跑掉。
