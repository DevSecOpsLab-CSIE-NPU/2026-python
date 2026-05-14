"""R01. CSV 基礎讀寫。

這份版本保留課堂示範的重點，並補上較完整的繁體中文註解，
方便直接閱讀 csv.reader、csv.DictReader、csv.writer、csv.DictWriter 的差異。
"""

import csv
import io


# 這裡用多行字串模擬一份 CSV 檔內容，方便直接在程式裡示範。
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""


# csv.reader：每一列會讀成 list，適合只想逐列處理原始資料的情況。
print("=== csv.reader ===")
f = io.StringIO(raw)
reader = csv.reader(f)
headers = next(reader)  # 先讀出第一列標題
print("標頭：", headers)
for row in reader:
    print(row)


# csv.DictReader：每一列會讀成 dict，欄位名稱會自動當成 key。
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
for row in csv.DictReader(f):
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")


# csv.writer：把 list 寫成 CSV 格式文字。
print("\n=== csv.writer ===")
output = io.StringIO()
writer = csv.writer(output)
writer.writerow(["Symbol", "Price", "Change"])
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])
print(output.getvalue())


# csv.DictWriter：把 dict 寫成 CSV，欄位順序由 fieldnames 決定。
print("=== csv.DictWriter ===")
output = io.StringIO()
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
writer.writeheader()
writer.writerow({"Symbol": "AA", "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
print(output.getvalue())


# 補充：常見參數的用途，實作時可依需求調整。
# delimiter='\t'   → 以 Tab 當分隔符號，常見於 TSV。
# quotechar='"'    → 指定引號字元。
# quoting=csv.QUOTE_ALL → 每個欄位都加上引號。
