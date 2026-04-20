# R11. 命名切片 slice（1.11）

# 定義一個字串 record，模擬一筆固定格式的資料記錄 (例如從舊式系統匯出的日誌)。
record = '....................100 .......513.25 ..........'
# 顯示原始記錄字串。
print(f"原始記錄字串 record: '{record}'")

# 使用 slice() 函式建立命名切片物件。這樣做可以避免在程式碼中散布著神祕的數字 (Magic Numbers)，提高可讀性。
# SHARES 定義了一個切片，從索引 20 開始（包含）到索引 23 結束（不包含），用於提取股票數量。
SHARES = slice(20, 23)
# PRICE 定義了一個切片，從索引 31 開始（包含）到索引 37 結束（不包含），用於提取股票價格。
PRICE = slice(31, 37)
# 顯示定義的命名切片。
print(f"定義命名切片 SHARES: {SHARES}")
print(f"定義命名切片 PRICE: {PRICE}\n")

# 使用命名切片從 record 字串中提取對應的子字串，並印出以供觀察。
print(f"從 record 中提取的股票數量 (字串): '{record[SHARES]}'")
print(f"從 record 中提取的股票價格 (字串): '{record[PRICE]}'\n")

# 將提取出的字串轉換為數值類型 (int 和 float)，並相乘計算總成本。
cost = int(record[SHARES]) * float(record[PRICE])
# 顯示計算出的總成本。
print(f"計算出的總成本 cost: {cost}")
