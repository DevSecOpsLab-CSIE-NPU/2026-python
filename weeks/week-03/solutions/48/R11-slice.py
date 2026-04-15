# R11. 命名切片 slice（1.11）

record = '....................100 .......513.25 ..........'
# 用具名 slice 取代魔術數字，提升可讀性
SHARES = slice(20, 23)
PRICE = slice(31, 37)
# 先切出欄位再轉型計算成本
cost = int(record[SHARES]) * float(record[PRICE])
