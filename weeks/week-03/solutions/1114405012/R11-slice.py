# R11. 命名切片 slice（1.11）

# 固定欄寬字串（股數與價格在固定位置）
record = '....................100 .......513.25 ..........'

# 用有名字的 slice 讓索引語意更清楚
SHARES = slice(20, 23)
PRICE = slice(31, 37)

shares = int(record[SHARES])
price = float(record[PRICE])
cost = shares * price

print('股數:', shares)
print('價格:', price)
print('總成本:', cost)
print('SHARES 範圍:', SHARES.start, SHARES.stop)
print('PRICE 範圍:', PRICE.start, PRICE.stop)
