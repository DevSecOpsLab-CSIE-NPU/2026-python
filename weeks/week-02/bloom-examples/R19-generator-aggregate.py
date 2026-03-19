"""R19: 生成器表達式 + 聚合函式。"""

nums = [1, 2, 3, 4, 5]
print('平方和:', sum(x * x for x in nums))

# join 只能接收字串，因此用生成器先做 str 轉換
record = ('ACME', 50, 123.45)
print('CSV 行:', ','.join(str(x) for x in record))

portfolio = [
    {'name': 'AOL', 'shares': 20},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'IBM', 'shares': 50},
]

print('最少股數:', min(s['shares'] for s in portfolio))
print('最少股數那筆資料:', min(portfolio, key=lambda s: s['shares']))
