"""R11: 用具名 slice 讓字串切片更可讀。"""

record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)

shares = int(record[SHARES])
price = float(record[PRICE])
cost = shares * price

print('shares:', shares)
print('price:', price)
print('cost:', cost)
