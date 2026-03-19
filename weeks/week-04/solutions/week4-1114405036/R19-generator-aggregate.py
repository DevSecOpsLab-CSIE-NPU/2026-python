# R19. 轉換 + 聚合：生成器表達式（1.19）
# 說明：在進行 sum(), min(), max() 等計算時直接轉換資料，不需要建立中介 list。

nums = [1, 2, 3, 4, 5]

# 1. 計算平方和
s_square = sum(x * x for x in nums) # 直接傳入生成器

# 2. 合併非字串序列為字串
s = ('ACME', 50, 123.45)
s_str = ','.join(str(x) for x in s) # 'ACME,50,123.45'

# 3. 根據字典中的特定欄位取最小值
portfolio = [
    {'name': 'AOL', 'shares': 20},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'FB', 'shares': 10}
]
min_shares = min(s['shares'] for s in portfolio) # 10
# 或是取得整個字典物件
min_item = min(portfolio, key=lambda s: s['shares']) # {'name': 'FB', 'shares': 10}