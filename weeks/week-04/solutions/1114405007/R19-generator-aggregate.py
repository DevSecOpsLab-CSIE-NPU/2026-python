# R19. 轉換+聚合：生成器表達式（1.19）

nums = [1, 2, 3]

# 把每個數字平方後直接交給 sum 加總，不需先建立中間串列
sum(x * x for x in nums)

s = ('ACME', 50, 123.45)

# 將不同型別的資料轉成字串後串接
','.join(str(x) for x in s)

portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]

# 只比較 shares 欄位的值，找出最小持股數
min(s['shares'] for s in portfolio)

# 直接找出 shares 最小的整筆字典資料
min(portfolio, key=lambda s: s['shares'])
