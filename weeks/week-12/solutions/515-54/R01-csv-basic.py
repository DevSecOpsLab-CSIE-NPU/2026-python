# R01. CSV 基礎讀寫（6.1）
# csv.reader / csv.writer / csv.DictReader / csv.DictWriter

import csv
import io

# ── 範例資料（模擬 CSV 字串）────────────────────────────
# 【詳解】
# CSV（Comma-Separated Values）是最常見的資料交換格式。
# 每行代表一筆記錄，各欄位間以逗號分隔。
# 第一行通常是欄位標頭（Column Names），便於程式自動對應。
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列是 list ───────────────
# 【詳解】
# csv.reader() 是最基本的讀取方式。它逐行解析 CSV 格式，
# 返回每行的欄位作為 list（列表）。各欄位都是字串型別，
# 若需要數值運算須手動轉型（如 float(row[1])）。
# next(reader) 手動取出下一行。這裡用它取得標頭行。
print("=== csv.reader ===")
f = io.StringIO(raw)
reader = csv.reader(f)
headers = next(reader) # 第一列當標頭
print("標頭：", headers)
for row in reader:
    print(row)

# ── 6.1 csv.DictReader：每列自動對應成 dict ──────────────
# 【詳解】
# csv.DictReader() 自動根據標頭行建立 dict（字典）。
# 存取欄位時可用名稱（row['Symbol']）而非索引（row[0]），
# 這樣程式碼更易讀、更不容易因改變欄位順序而出錯。
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
for row in csv.DictReader(f):
    print(f"{row['Symbol']:5s} 價格={row['Price']:>6s} 漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV ─────────────────────────────
# 【詳解】
# csv.writer() 用來寫出 CSV 格式資料。writerow() 接收 list，
# 自動加上分隔符號（預設逗號）與換行。這裡用 StringIO 模擬
# 寫入檔案的過程，實務上應搭配 open() 寫入真實檔案。
print("\n=== csv.writer ===")
output = io.StringIO()
writer = csv.writer(output)
writer.writerow(["Symbol", "Price", "Change"])
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])
print(output.getvalue())

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV ─────────────────
# 【詳解】
# csv.DictWriter() 搭配 dict 使用。需先指定 fieldnames
# （欄位順序），writeheader() 寫標頭，writerow(dict) 寫資料。
# 好處是資料來源若已是 dict（如資料庫查詢結果），可直接傳入。
print("=== csv.DictWriter ===")
output = io.StringIO()
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
writer.writeheader()
writer.writerow({"Symbol": "AA", "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
print(output.getvalue())

# ── 常用參數 ─────────────────────────────────────────────
# 【詳解】
# delimiter='\t' → 用 Tab 而非逗號分隔（TSV 格式）
# quotechar='"' → 指定引號字元（預設雙引號）
# quoting=csv.QUOTE_ALL → 每個欄位都加引號（避免內含逗號誤解析）
# newline='' 需搭配 open() 使用，避免 Windows 多出空行
# encoding='utf-8-sig' → UTF-8 with BOM，相容 Excel 開啟中文
# delimiter='\t' → TSV（Tab 分隔）
# quotechar='"' → 引號字元
# quoting=csv.QUOTE_ALL → 每個欄位都加引號（避免值中有逗號造成誤解析）
