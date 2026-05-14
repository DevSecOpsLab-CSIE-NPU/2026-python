# R01. CSV 基礎讀寫（6.1）
# csv.reader / csv.writer / csv.DictReader / csv.DictWriter
#
# 這個範例的目的，是示範 Python 標準函式庫 csv 模組最常見的四種用法：
# 1. 用 csv.reader 逐列讀取 CSV，資料會以 list 形式出現。
# 2. 用 csv.DictReader 讀取 CSV，資料會以 dict 形式出現，欄位名稱更好理解。
# 3. 用 csv.writer 寫出 CSV，適合資料來源已經是 list / tuple 的情境。
# 4. 用 csv.DictWriter 寫出 CSV，適合資料來源已經是 dict 的情境。

import csv
import io

# ── 範例資料（模擬 CSV 字串）────────────────────────────
# 這裡不直接讀檔，而是先把 CSV 內容放進多行字串。
# 這樣做的好處是：
# - 可以直接在程式中看到資料長什麼樣子。
# - 不需要另外準備檔案，方便教學與測試。
# - 後面搭配 io.StringIO，就能把字串假裝成「檔案物件」來使用。
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列是 list ───────────────
# csv.reader 的回傳結果是一個可迭代物件。
# 每次迭代都會拿到一列資料，而每一列會被拆成欄位清單（list）。
# 這種方式最接近「原始 CSV」的樣貌，適合你想自行處理每個欄位時使用。
print("=== csv.reader ===")
# StringIO 會把字串包成像檔案一樣的物件，讓 csv.reader 可以直接讀取。
f = io.StringIO(raw)
reader = csv.reader(f)
# next(reader) 會先讀出第一列，也就是標頭列。
# 常見做法是先把欄位名稱取出來，後面就能分開處理真正的資料列。
headers = next(reader)          # 第一列當標頭
print("標頭：", headers)
# 從第二列開始，每一列都是一筆資料，這裡直接把 list 印出來，方便觀察結構。
for row in reader:
    print(row)

# ── 6.1 csv.DictReader：每列自動對應成 dict ──────────────
# DictReader 會自動把第一列當作欄位名稱，
# 接下來每一列資料會轉成 dict，例如 {'Symbol': 'AA', 'Price': '39.48', ...}。
# 這樣在程式中取值時可以直接用欄位名稱，比索引位置更直覺，也更不容易寫錯。
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
# 因為 DictReader 已經知道標頭，所以不需要先 next()。
# 迴圈中的 row 會是一個 dict，適合用欄位名稱做格式化輸出。
for row in csv.DictReader(f):
    # 這裡示範如何直接取出指定欄位，並搭配格式化字串控制輸出寬度。
    # 注意：CSV 讀進來的值預設都是字串，所以 row['Price'] 的型別也是字串。
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV ─────────────────────────────
# writer 用來把資料寫成 CSV 格式。
# 如果你的資料本來就是 list 或 tuple，writer 會是最直接的選擇。
# 寫入到 StringIO 後，可以立刻用 getvalue() 看到輸出的 CSV 字串。
print("\n=== csv.writer ===")
# 同樣先準備一個字串緩衝區，讓寫出的內容留在記憶體中，不需要真的存檔。
output = io.StringIO()
writer = csv.writer(output)
# writerow() 每呼叫一次，就會寫入一列資料。
# 第一列通常放欄位名稱，讓 CSV 更容易被人或其他程式理解。
writer.writerow(["Symbol", "Price", "Change"])
# 下面兩列是實際資料，writer 會自動幫你處理 CSV 格式的分隔與換行。
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])
# getvalue() 會把目前緩衝區中的所有內容取出，方便直接印出檢查結果。
print(output.getvalue())

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV ─────────────────
# DictWriter 適合你手上已有 dict 資料的情況。
# 先指定 fieldnames（欄位順序），再用 writeheader() 輸出表頭，
# 最後用 writerow() 依照欄位名稱寫入各筆資料。
print("=== csv.DictWriter ===")
output = io.StringIO()
# fieldnames 決定欄位的順序，也決定 writeheader() 會輸出哪些標題。
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
# writeheader() 會根據 fieldnames 自動寫出標頭列。
writer.writeheader()
# 傳入 dict 時，鍵名會對應到欄位名稱；值則是要寫出的資料內容。
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
# 和 writer 一樣，最後用 getvalue() 看到整份輸出的 CSV 字串。
print(output.getvalue())

# ── 常用參數 ─────────────────────────────────────────────
# 下面列出幾個最常調整的 csv 參數：
# delimiter='\t'：把欄位分隔符號改成 Tab，這樣就會變成 TSV（Tab Separated Values）。
# quotechar='"'：指定欄位內容需要引用時，使用哪一個字元包住內容。
# quoting=csv.QUOTE_ALL：輸出時每個欄位都加上引號，適合資料內容可能包含逗號、換行或空白的情況。
