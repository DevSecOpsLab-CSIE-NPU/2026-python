# R11. 命名切片 slice（1.11）

# 一段固定格式的字串紀錄（例如：股票交易紀錄）
record = '....................100 .......513.25 ..........'

# 使用 slice() 建立「命名切片」
# SHARES = 從索引 20 到 23（不含 23）
SHARES = slice(20, 23)

# PRICE = 從索引 31 到 37（不含 37）
PRICE = slice(31, 37)

# 使用命名切片來取出資料，比直接寫 record[20:23] 更易讀、可維護
cost = int(record[SHARES]) * float(record[PRICE])