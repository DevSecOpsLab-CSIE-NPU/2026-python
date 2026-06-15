# R01. CSV 基礎讀寫（6.1）
# csv.reader / csv.writer / csv.DictReader / csv.DictWriter
#
# CSV（Comma-Separated Values）是最通用的表格資料交換格式。
# Python 標準庫的 csv 模組提供四個主要工具：
#   reader/writer      → 以 list 為單位操作，適合結構簡單的資料
#   DictReader/DictWriter → 以 dict 為單位，欄位名稱即鍵值，可讀性更高

import csv
import io

# ── 範例資料（模擬 CSV 字串）────────────────────────────
# 用 io.StringIO 把字串「包裝成」類檔案物件，
# 讓 csv.reader 以為自己在讀一個真實的檔案，方便測試或記憶體內操作。
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列是 list ───────────────
print("=== csv.reader ===")
f = io.StringIO(raw)
reader = csv.reader(f)         # 回傳 reader 物件，本身是迭代器
headers = next(reader)         # 呼叫 next() 取出第一列作為標頭
print("標頭：", headers)        # ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
for row in reader:             # 剩下的列逐一讀取，每列是 list[str]
    print(row)

# ── 6.1 csv.DictReader：每列自動對應成 dict ──────────────
# DictReader 會自動把第一列當作欄位名稱（fieldnames），
# 後續每列回傳 dict，可用欄位名稱直接索引，比 list 的索引數字更直覺。
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
for row in csv.DictReader(f):
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV ─────────────────────────────
# csv.writer 接受任何類檔案物件（file-like object）。
# 這裡用 StringIO 把輸出暫存在記憶體，方便示範。
print("\n=== csv.writer ===")
output = io.StringIO()
writer = csv.writer(output)
writer.writerow(["Symbol", "Price", "Change"])  # 先寫標頭列
writer.writerow(["AA", 39.48, -0.18])            # 再寫資料列
writer.writerow(["AIG", 71.38, -0.15])
print(output.getvalue())                         # 取出最終字串

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV ─────────────────
# DictWriter 需要先宣告 fieldnames，確保每列的欄位順序一致。
print("=== csv.DictWriter ===")
output = io.StringIO()
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
writer.writeheader()                                         # 自動根據 fieldnames 寫標頭
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
print(output.getvalue())

# ── 常用參數 ─────────────────────────────────────────────
# delimiter='\t'        → TSV（Tab 分隔），適合儲存含逗號的欄位
# quotechar='"'         → 引號字元（預設即 ""）
# quoting=csv.QUOTE_ALL → 每個欄位都強制加引號，避免特殊字元誤判
