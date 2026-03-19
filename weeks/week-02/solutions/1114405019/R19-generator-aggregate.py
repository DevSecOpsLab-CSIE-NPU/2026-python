# R19. 轉換+聚合：生成器表達式（1.19）

nums = [1, 2, 3]
sum(x * x for x in nums)

s = ('ACME', 50, 123.45)
','.join(str(x) for x in s)

portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]
min(s['shares'] for s in portfolio)
min(portfolio, key=lambda s: s['shares'])
