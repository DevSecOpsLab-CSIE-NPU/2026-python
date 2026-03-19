# R19. 轉換+聚合：生成器表達式（1.19）
#
# 觀念重點：
# - 生成器表達式常搭配 sum/min/max/join 等聚合函式。
# - 它不先建立完整中間 list，記憶體使用通常更省。

nums = [1, 2, 3]

# 先把每個數字平方，再做總和。
sum(x * x for x in nums)

s = ('ACME', 50, 123.45)

# 先把每個元素轉字串，再用逗號串接。
','.join(str(x) for x in s)

portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]

# 只比較 shares 值，得到最小持股數。
min(s['shares'] for s in portfolio)

# 直接回傳「整筆字典資料」中 shares 最小者。
min(portfolio, key=lambda s: s['shares'])
