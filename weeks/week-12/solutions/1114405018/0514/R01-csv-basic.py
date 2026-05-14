"""R01. CSV 基礎讀寫（6.1）

說明（繁體中文詳細註解）：
- 本檔示範 Python 標準函式庫 `csv` 的常見用法：`reader`、`DictReader`、`writer`、`DictWriter`。
- 重要概念：CSV 是純文字格式，欄位以分隔符分隔。讀取時會把每列解析為 list 或 dict；寫出時需注意欄位順序與轉型（數字預設為字串）。

使用情境與注意事項：
- 若要處理大量資料建議用檔案對象（open(file, 'r', encoding='utf-8')）搭配 `csv.reader`，避免一次把整個檔案讀進記憶體。
- `DictReader` 會把第一列當作欄位名稱（header），並把每列轉成 dict，key 為欄位名稱，對於欄位較多或順序不定時更好用。
- 寫出時若要確保非 ASCII 字元正確呈現，需指定檔案編碼 `encoding='utf-8'`。
"""

import csv
import io


# 範例資料（模擬 CSV 字串）
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""


# csv.reader：逐列讀取，回傳 iterator，每列為 list
print("=== csv.reader ===")
f = io.StringIO(raw)
reader = csv.reader(f)
headers = next(reader)          # 第一列為 header（欄位名稱）
print("標頭：", headers)
for row in reader:
    # 每個 row 的每個欄位都是字串（需要時再轉型 int/float）
    print(row)


# csv.DictReader：把每列對應成 dict（key = header）
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
for row in csv.DictReader(f):
    # 以欄位名稱存取，較不會受欄位順序影響，對資料清洗較友善
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")


# csv.writer：將資料寫回 CSV（每列以 list 方式提供）
print("\n=== csv.writer ===")
output = io.StringIO()
writer = csv.writer(output)
writer.writerow(["Symbol", "Price", "Change"])   # header
writer.writerow(["AA", 39.48, -0.18])                 # 注意：writer 會把非字串轉為字串寫出
writer.writerow(["AIG", 71.38, -0.15])
print(output.getvalue())


# csv.DictWriter：以 dict 寫出 CSV，需提供 fieldnames 保持欄位順序一致
print("=== csv.DictWriter ===")
output = io.StringIO()
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
writer.writeheader()
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
print(output.getvalue())


# 常用參數補充：
# - delimiter='\t'   → TSV（Tab 分隔）
# - quotechar='"'    → 指定包覆字元（當欄位內含 delimiter 或換行時會自動加上）
# - quoting=csv.QUOTE_ALL → 每個欄位都加引號
# - newline='' 在 open() 時使用可避免 Windows 下空行問題（搭配 csv.writer）
