# R19. 轉換 + 聚合：生成器表達式（1.19）

nums = [1, 2, 3]

# 生成器表達式可直接丟給 sum，不需要先建立中間清單
sum_of_squares = sum(x * x for x in nums)

s = ('ACME', 50, 123.45)

# join 需要字串，因此先把每個元素轉成 str
csv_line = ','.join(str(x) for x in s)

portfolio = [
    {'name': 'AOL', 'shares': 20},
    {'name': 'YHOO', 'shares': 75},
]

# 只拿 shares 做聚合（回傳最小持股數）
min_shares = min(item['shares'] for item in portfolio)

# 若想拿到整筆資料，使用 key 參數
min_shares_item = min(portfolio, key=lambda item: item['shares'])
