"""R19. 轉換+聚合：生成器表達式（1.19）

示範如何使用生成器表達式（generator expression）作為轉換與聚合的有效寫法。
"""

nums = [1, 2, 3]

# sum 可以直接接受生成器表達式，不需要先建立中間列表
sum(x * x for x in nums)

s = ('ACME', 50, 123.45)

# 透過生成器將元素轉為字串並以逗號連接
','.join(str(x) for x in s)

portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]

# 找到最小 shares 的值（使用生成器表達式)
min(s['shares'] for s in portfolio)

# 直接找出 shares 最小的整個 dict（使用 key 參數） 
min(portfolio, key=lambda s: s['shares'])
