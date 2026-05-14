# R01. CSV 基礎讀寫（6.1）
# 範圍：示範 `csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter` 的基本使用
# 註解語言：繁體中文（臺灣 zh-TW），並補充每個步驟的用途、資料型態與常見錯誤

import csv
import io

# ── 範例資料（模擬 CSV 字串）────────────────────────────
# 為了教學方便，我們用一個記憶體中的字串來模擬從檔案讀入的 CSV 內容。
# 這樣可以直接在程式中展示「讀取」與「寫出」的流程，而不必先準備外部檔案。
# 每一列以換行符號分隔，第一列是欄位名稱（header），後面的列則是實際資料。
# 注意：實務上若從檔案讀取，建議開檔時使用 `open(filename, newline='', encoding='utf-8')`，
# 這樣可以避免在 Windows 上出現多餘空行，也能確保中文或其他非 ASCII 字元正確顯示。
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列會被解析成 list ───────────────
# 用法說明：
# - `csv.reader` 會把每一列拆成一個 list，而且所有欄位預設都會是字串。
# - 若 CSV 第一列為欄位名稱，可以先用 `next(reader)` 讀出來，這一列通常會被拿來當作標頭。
# - 因為 CSV 檔本質上只保存文字，所以像價格、數量這類欄位如果要做運算，必須自己轉型。
# - 也就是說，`row[1]` 看起來像數字，但實際上仍是字串 `'39.48'`，不能直接當成浮點數計算。
print("=== csv.reader ===")
f = io.StringIO(raw)           # 用 StringIO 模擬檔案物件
reader = csv.reader(f)        # 產生器，逐列回傳 list
headers = next(reader)        # 讀取第一列作為欄位名稱
print("標頭：", headers)
for row in reader:
    # row 範例： ['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800']
    # 這裡直接把 list 印出來，目的就是讓你看到 CSV 被拆欄後的實際結構。
    print(row)

# ── 6.1 csv.DictReader：每列自動對應成 dict（欄位名稱 -> 欄位值） ──────────────
# 用法說明：
# - `csv.DictReader` 會自動把每列以欄位名稱當作 key，回傳 dict（所有值皆為字串）。
# - 這種方式的好處是欄位存取更直觀，不必記住欄位在第幾個位置。
# - 存取欄位時使用 `row['Symbol']`、`row['Price']` 等；若要做數值運算，請先轉型。
# - 若 CSV 檔沒有 header，可在建立 DictReader 時傳入 `fieldnames=[...]`，由你手動指定欄位名稱。
print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
for row in csv.DictReader(f):
    # 取出欄位並格式化輸出：注意取出的都是字串，所以欄位寬度與對齊要靠格式化字串處理。
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV（以 list 形式寫入每一列） ─────────────────────────────
# 用法說明：
# - `csv.writer` 的 `writerow()` 接受一個可迭代物件（例如 list/tuple），並把每個元素寫成一個欄位。
# - 若傳入的資料是數值，writer 會自動把它轉成字串再寫入，因此不用先手動 `str()`。
# - 在寫入檔案時，建議用 `open(filename, 'w', newline='', encoding='utf-8')`，
#   這是 Python CSV 模組常見的標準寫法，可以避免在 Windows 平台上出現空白列的問題。
print("\n=== csv.writer ===")
output = io.StringIO()
writer = csv.writer(output)
# 寫入標頭列：這一列的順序會影響整個 CSV 檔的欄位排列。
writer.writerow(["Symbol", "Price", "Change"])
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])
# `getvalue()` 會把 `StringIO` 內部累積的 CSV 內容一次取出，方便我們直接在螢幕上檢查結果。
print(output.getvalue())

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV（以欄位名稱為基準） ─────────────────
# 用法說明：
# - 建立時需提供 `fieldnames`（欄位順序會依此輸出），因此它同時控制「欄位名稱」與「輸出順序」。
# - 使用 `writeheader()` 可以輸出欄位名稱列，通常會放在 CSV 最上方。
# - `writerow()` 接受一個 dict，鍵對應到欄位名稱；若某些 key 缺失，輸出的欄位就會是空白。
# - 若輸入 dict 含有未列在 `fieldnames` 的鍵，可用 `extrasaction='ignore'` 或 `'raise'` 處理，
#   前者會忽略多餘欄位，後者則直接丟出錯誤，方便除錯。
print("=== csv.DictWriter ===")
output = io.StringIO()
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
writer.writeheader()
# 這裡示範用 dict 寫資料，比 `writer.writerow([...])` 更容易看出欄位與值的對應關係。
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
# 直接印出結果，讓你確認欄位順序與內容是否符合預期。
print(output.getvalue())

# ── 常用參數與注意事項 ─────────────────────────────────────────────
# - `delimiter=','`（預設）: 欄位分隔符，若要處理 TSV 可指定 `delimiter='\t'`。
# - `quotechar='"'`（預設）: 欄位包起來的引號字元，當欄位內含分隔符或換行時特別重要。
# - `quoting=csv.QUOTE_ALL` / `csv.QUOTE_MINIMAL` / `csv.QUOTE_NONNUMERIC` 等，控制何時加引號，
#   可依資料來源與對外格式需求選擇。
# - 開啟檔案時務必使用 `newline=''`（寫入/讀取皆是），避免在某些平台看到雙倍換行或空行。
# - 若要處理非 UTF-8 編碼的檔案，請在 open 時指定 `encoding`，或在讀入後做編碼轉換。
# - CSV 模組不會自動把數字轉型（全部都當字串），需要自行用 `int()` / `float()` 轉換。
# - 如果欄位內容可能包含逗號、引號或換行，CSV 模組會依規則幫你跳脫，但前提是資料必須透過模組寫入。
