# R11 slice
# 目標：使用具名切片提升可讀性，避免硬編碼索引。

record = "....................100 .......513.25 .........."

# 用 slice 命名欄位區間，比寫死 [20:23] 更清楚
SHARES = slice(20, 23)
PRICE = slice(31, 37)

cost = int(record[SHARES]) * float(record[PRICE])
