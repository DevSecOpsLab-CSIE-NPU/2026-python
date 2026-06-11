# R01-csv-basic.py
# 完整繁體中文註釋版：示範 csv.reader / csv.writer / csv.DictReader / csv.DictWriter

import csv
import io

# ── 範例 CSV 字串（模擬檔案內容）────────────────────────────
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── csv.reader：讀取每列為 list
print("=== csv.reader ===")
f = io.StringIO(raw)           # 把字串當成檔案物件
reader = csv.reader(f)
headers = next(reader)         # 第一列視為標頭
print("標頭：", headers)
for row in reader:
    print(row)

# ── csv.DictReader：每列自動對應成 dict
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
for row in csv.DictReader(f):
    # 每一列會變成 dict，欄位名稱當 key
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── csv.writer：將資料寫回 CSV 格式
print("\n=== csv.writer ===")
output = io.StringIO()
writer = csv.writer(output)
writer.writerow(["Symbol", "Price", "Change"])
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])
print(output.getvalue())

# ── csv.DictWriter：以 dict 寫出 CSV
print("=== csv.DictWriter ===")
output = io.StringIO()
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
writer.writeheader()
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
print(output.getvalue())

# ── 常用參數說明 ─────────────────────────────────────────
# delimiter='\t'    → 產生 TSV（制表符分隔）
# quotechar='"'     → 設定欄位引號字元
# quoting=csv.QUOTE_ALL → 所有欄位都加引號
