# R01. CSV 基礎讀寫（6.1）
# 本示例展示了 CSV 檔案的四種主要讀寫方式：
# 1. csv.reader：逐列讀取，每列作為 list（按位置存取）
# 2. csv.DictReader：逐列讀取，每列作為 dict（按欄位名存取）
# 3. csv.writer：逐列寫出，接受 list 格式
# 4. csv.DictWriter：逐列寫出，接受 dict 格式

import csv  # 標準庫：CSV 檔案處理
import io   # 標準庫：記憶體中的文字 I/O 操作（用來模擬檔案）

# ── 範例資料（模擬 CSV 字串）────────────────────────────
# CSV (Comma-Separated Values) 是純文字格式，用逗號分隔欄位
# 第一列通常是標頭，描述各欄位的名稱
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列是 list ───────────────
# csv.reader() 返回一個迭代器，每次迭代返回一列資料（以 list 形式）
# 優點：依次讀取，記憶體佔用少；缺點：需要記住欄位位置
print("=== csv.reader ===")
f = io.StringIO(raw)  # 將字串作為類檔案物件
reader = csv.reader(f)  # 建立 CSV 讀取器
headers = next(reader)  # 使用 next() 讀取第一列作為標頭（此後不再讀取）
print("標頭：", headers)  # 預期輸出：['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
for row in reader:  # 迴圈遍歷剩餘列
    print(row)  # 每行是一個 list，例如 ['AA', '39.48', '6/11/2007', ...]

# ── 6.1 csv.DictReader：每列自動對應成 dict ──────────────
# csv.DictReader() 自動將第一列視為欄位名，之後每列返回一個 dict
# 優點：可按欄位名存取資料，程式碼易讀；缺點：記憶體占用多
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)  # 重新建立類檔案物件（因為前面已讀完）
for row in csv.DictReader(f):  # 直接迭代，自動處理標頭
    # 每一行 row 是一個 dict，格式為：
    # {'Symbol': 'AA', 'Price': '39.48', 'Date': '6/11/2007', ...}
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV ─────────────────────────────
# csv.writer() 用於將資料寫成 CSV 格式
# writerow() 接受一個 list，自動加上逗號和正確的引號（如果需要）
# 優點：簡單直接，不需要手動拼接逗號；缺點：必須處理 list 順序
print("\n=== csv.writer ===")
output = io.StringIO()  # 建立記憶體中的字串緩衝區
writer = csv.writer(output)  # 建立 CSV 寫入器
writer.writerow(["Symbol", "Price", "Change"])  # 寫入標頭列
writer.writerow(["AA", 39.48, -0.18])  # 寫入資料列
writer.writerow(["AIG", 71.38, -0.15])  # 注意：數字會自動轉換為字串
print(output.getvalue())  # 預期輸出："Symbol,Price,Change\nAA,39.48,-0.18\nAIG,..."

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV ─────────────────
# csv.DictWriter() 用於將字典資料寫成 CSV 格式
# fieldnames 參數定義欄位順序和名稱
# writeheader() 寫入標頭列；writerow() 接受 dict 並按 fieldnames 順序寫出
# 優點：易於管理具名欄位的資料；缺點：需要指定 fieldnames
print("=== csv.DictWriter ===")
output = io.StringIO()  # 建立記憶體中的字串緩衝區
fieldnames = ["Symbol", "Price", "Change"]  # 定義欄位順序
writer = csv.DictWriter(output, fieldnames=fieldnames)  # 建立 DictWriter
writer.writeheader()  # 寫入標頭列（第一行）
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})  # 寫入資料列
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})  # dict 可不按 fieldnames 順序
print(output.getvalue())  # 預期輸出："Symbol,Price,Change\nAA,39.48,-0.18\nAIG,..."

# ── 常用參數 ─────────────────────────────────────────────
# delimiter='\t'   → 改用 Tab 分隔（TSV 格式）
#   例如：csv.reader(f, delimiter='\t')
# quotechar='"'    → 定義引號字元（預設為雙引號）
#   用於包含特殊字元（如逗號、換行）的欄位
# quoting=csv.QUOTE_ALL → 每個欄位都加引號
# quoting=csv.QUOTE_MINIMAL → 只在需要時加引號（預設）
# quoting=csv.QUOTE_NONNUMERIC → 非數字欄位加引號
# 例子：
#   writer = csv.writer(output, delimiter='\t', quoting=csv.QUOTE_ALL)
#   reader = csv.reader(f, delimiter='|', quotechar="'")
