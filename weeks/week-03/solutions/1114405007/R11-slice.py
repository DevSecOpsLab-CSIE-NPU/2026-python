# R11: slice 物件
# 觀念：用具名 slice 取代魔法數字，讓固定欄位切片更可讀。

record = '....................100 .......513.25 ..........'

# 20~22 字元代表股數，31~36 字元代表價格（右界不含）
SHARES = slice(20, 23)
PRICE = slice(31, 37)

# 可讀性更高：record[SHARES]、record[PRICE]
cost = int(record[SHARES]) * float(record[PRICE])
