# R01. CSV 基礎讀寫（6.1）
# csv.reader / csv.writer / csv.DictReader / csv.DictWriter

import csv
import io

# ── 範例資料（模擬 CSV 字串）────────────────────────────
# 這裡直接用字串模擬 CSV 檔案內容，方便示範讀寫流程。
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列是 list ───────────────
print("=== csv.reader ===")
f = io.StringIO(raw)
reader = csv.reader(f)
headers = next(reader)          # 第一列當標頭
# 先把標頭讀出來，後面每一列資料就可以對照欄位名稱。
print("標頭：", headers)
for row in reader:
    # reader 讀到的是 list，所以每一欄都要用索引存取。
    print(row)

# ── 6.1 csv.DictReader：每列自動對應成 dict ──────────────
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
for row in csv.DictReader(f):
    # DictReader 會把每列轉成 dict，因此可以直接用欄位名稱取值。
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV ─────────────────────────────
print("\n=== csv.writer ===")
output = io.StringIO()
writer = csv.writer(output)
# 先寫標頭，再逐列寫入資料。
writer.writerow(["Symbol", "Price", "Change"])
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])
print(output.getvalue())

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV ─────────────────
print("=== csv.DictWriter ===")
output = io.StringIO()
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
# DictWriter 需要先知道欄位順序，才能正確輸出表頭與資料。
writer.writeheader()
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
print(output.getvalue())

# ── 常用參數 ─────────────────────────────────────────────
# delimiter='\t'   → TSV（Tab 分隔）
# quotechar='"'    → 引號字元
# quoting=csv.QUOTE_ALL → 每個欄位都加引號
