# R01. CSV 基礎讀寫（6.1）
# csv.reader / csv.writer / csv.DictReader / csv.DictWriter

import csv
import io

# ── 範例資料（模擬 CSV 字串）────────────────────────────
# 使用多行字串建立一個模擬的 CSV 檔案內容
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列是 list ───────────────
print("=== csv.reader ===")
# io.StringIO 可以將字串包裝成像檔案一樣的操作介面
f = io.StringIO(raw)
# csv.reader 會將讀取到的每一列轉換為 Python 的 list
reader = csv.reader(f)
# 使用 next() 讀取第一列，通常 CSV 的第一列是標頭（欄位名稱）
headers = next(reader)          # 第一列當標頭
print("標頭：", headers)
# 接下來的迴圈會從第二列開始逐列讀取資料
for row in reader:
    print(row)

# ── 6.1 csv.DictReader：每列自動對應成 dict ──────────────
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
# csv.DictReader 會自動把第一列當作 key，將每一列資料轉換成字典 (dict)
for row in csv.DictReader(f):
    # 透過字典的 key 來取得對應欄位的值，不僅好讀且不怕欄位順序改變
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV ─────────────────────────────
print("\n=== csv.writer ===")
# 建立一個寫入用的記憶體字串緩衝區
output = io.StringIO()
# 建立 csv.writer 物件，準備寫入資料
writer = csv.writer(output)
# 寫入第一列（標頭）
writer.writerow(["Symbol", "Price", "Change"])
# 寫入資料列（必須傳入 list）
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])
# getvalue() 可以取得目前緩衝區內累積的所有字串
print(output.getvalue())

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV ─────────────────
print("=== csv.DictWriter ===")
output = io.StringIO()
# 必須先定義好標頭欄位清單
fieldnames = ["Symbol", "Price", "Change"]
# 建立 csv.DictWriter 物件，並傳入標頭欄位清單
writer = csv.DictWriter(output, fieldnames=fieldnames)
# writeheader() 會自動把 fieldnames 寫成第一列
writer.writeheader()
# 使用字典格式寫入資料列，欄位順序可與 fieldnames 不同，且可讀性較高
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
print(output.getvalue())

# ── 常用參數 ─────────────────────────────────────────────
# delimiter='\t'        → TSV（Tab 分隔），指定欄位的分隔符號
# quotechar='"'         → 引號字元，當欄位內容包含分隔符號時使用的包裝字元
# quoting=csv.QUOTE_ALL → 強制每個欄位輸出時都加上引號
