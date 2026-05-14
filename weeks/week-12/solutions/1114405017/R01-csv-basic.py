# R01. CSV 基礎讀寫（6.1）
# csv.reader / csv.writer / csv.DictReader / csv.DictWriter

# 匯入必要的模組
import csv  # 用於處理CSV檔案的標準庫模組
import io   # 用於處理字串輸入輸出

# ── 範例資料（模擬 CSV 字串）────────────────────────────
# 定義一個包含股票資料的CSV格式字串
# 這個字串模擬從檔案讀取的CSV內容，包含標頭和資料列
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列是 list ───────────────
# 使用csv.reader來讀取CSV資料
# csv.reader會將每一列解析為一個list，每個元素對應一個欄位
print("=== csv.reader ===")
f = io.StringIO(raw)  # 將字串轉換為檔案-like物件，以便csv.reader處理
reader = csv.reader(f)  # 建立CSV讀取器
headers = next(reader)  # 讀取第一列作為標頭（next()會移動到下一列）
print("標頭：", headers)  # 輸出標頭欄位
for row in reader:  # 逐列讀取剩餘的資料列
    print(row)  # 輸出每一列的資料（以list形式）

# ── 6.1 csv.DictReader：每列自動對應成 dict ──────────────
# 使用csv.DictReader來讀取CSV資料
# csv.DictReader會將每一列解析為一個dict，鍵為標頭欄位名稱，值為對應的資料
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)  # 重新建立字串輸入物件
for row in csv.DictReader(f):  # 直接迭代DictReader，每一列都是dict
    # 使用格式化字串輸出特定欄位的資料
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV ─────────────────────────────
# 使用csv.writer來寫出CSV資料
# csv.writer會將list寫入為CSV格式的列
print("\n=== csv.writer ===")
output = io.StringIO()  # 建立字串輸出物件來儲存寫出的CSV內容
writer = csv.writer(output)  # 建立CSV寫入器
writer.writerow(["Symbol", "Price", "Change"])  # 寫入標頭列
writer.writerow(["AA", 39.48, -0.18])  # 寫入第一筆資料
writer.writerow(["AIG", 71.38, -0.15])  # 寫入第二筆資料
print(output.getvalue())  # 輸出寫出的CSV字串

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV ─────────────────
# 使用csv.DictWriter來寫出CSV資料
# csv.DictWriter會將dict寫入為CSV格式的列，需要指定欄位名稱順序
print("=== csv.DictWriter ===")
output = io.StringIO()  # 建立字串輸出物件
fieldnames = ["Symbol", "Price", "Change"]  # 定義欄位名稱順序
writer = csv.DictWriter(output, fieldnames=fieldnames)  # 建立DictWriter
writer.writeheader()  # 寫入標頭列
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})  # 寫入第一筆資料（dict）
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})  # 寫入第二筆資料
print(output.getvalue())  # 輸出寫出的CSV字串

# ── 常用參數 ─────────────────────────────────────────────
# csv模組的常用參數設定：
# delimiter='\t'   → 使用Tab字元作為分隔符號，適用於TSV（Tab分隔值）檔案
# quotechar='"'    → 指定引號字元，預設為雙引號
# quoting=csv.QUOTE_ALL → 設定所有欄位都加上引號，確保特殊字元不會干擾解析
