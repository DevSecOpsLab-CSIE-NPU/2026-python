# R11. 命名切片 slice（1.11）

record = '....................100 .......513.25 ..........'
# 用具名 slice 讓固定欄位切片更可讀
SHARES = slice(20, 23)
PRICE = slice(31, 37)

# 取出股數與價格後計算成本
cost = int(record[SHARES]) * float(record[PRICE])
