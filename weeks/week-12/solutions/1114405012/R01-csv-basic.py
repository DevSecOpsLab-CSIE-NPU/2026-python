# R01. CSV 基礎讀寫（6.1）
# csv.reader / csv.writer / csv.DictReader / csv.DictWriter

import csv
import io

# 這份示範重點：
# 1) 如何把「CSV 文字」當作檔案讀進來
# 2) 如何用 reader / DictReader 讀資料
# 3) 如何用 writer / DictWriter 寫資料
# 4) 四種 API 各自適用情境

# ── 範例資料（模擬 CSV 字串）────────────────────────────
# 實務上通常會從 .csv 檔案讀取，這裡用三引號字串模擬檔案內容，
# 方便在單一腳本中直接觀察結果。
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列是 list ───────────────
print("=== csv.reader ===")
# io.StringIO 可以把「字串」包裝成「類檔案物件」，
# 讓 csv.reader 像讀真實檔案一樣讀它。
f = io.StringIO(raw)
# reader 會逐行解析 CSV；每次迭代得到的是 list（依欄位順序）。
reader = csv.reader(f)
# next(reader) 先取出第一列（標頭列），避免下面 for 迴圈把它當資料列。
headers = next(reader)
print("標頭：", headers)
# 後續每一列都會是 list，例如：['AA', '39.48', '6/11/2007', ...]
for row in reader:
    print(row)

# ── 6.1 csv.DictReader：每列自動對應成 dict ──────────────
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
# DictReader 會把第一列當欄位名，後續每列轉為 dict：
# key=欄位名（例如 Symbol），value=該列對應值。
for row in csv.DictReader(f):
    # 這裡示範字串格式化：
    # {row['Symbol']:5s}  代表 Symbol 欄位用寬度 5 左對齊
    # {row['Price']:>6s}  代表 Price 欄位用寬度 6 右對齊
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV ─────────────────────────────
print("\n=== csv.writer ===")
# 用 StringIO 接收輸出，等同「把 CSV 寫到記憶體」而非實體檔案。
output = io.StringIO()
# writerow 需要 list/tuple，欄位順序由你提供的序列決定。
writer = csv.writer(output)
# 先寫標頭列
writer.writerow(["Symbol", "Price", "Change"])
# 再寫資料列
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])
# getvalue() 取出目前整份 CSV 文字
print(output.getvalue())

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV ─────────────────
print("=== csv.DictWriter ===")
output = io.StringIO()
# fieldnames 決定輸出的欄位順序，也是 DictWriter 的必要參數。
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
# writeheader() 會依 fieldnames 輸出標頭列
writer.writeheader()
# writerow 接收 dict，key 對應欄位名；缺欄位或多欄位可再搭配參數控制。
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
print(output.getvalue())

# ── 常用參數 ─────────────────────────────────────────────
# delimiter='\t'   → TSV（Tab 分隔）
# quotechar='"'    → 引號字元
# quoting=csv.QUOTE_ALL → 每個欄位都加引號
# 補充：
# - 讀寫真實檔案時，建議使用 open(..., newline='', encoding='utf-8')
# - 如果 CSV 內含逗號、換行等特殊字元，csv 模組會自動處理引號與跳脫
