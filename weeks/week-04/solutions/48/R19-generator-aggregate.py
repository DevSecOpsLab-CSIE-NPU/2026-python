# R19. 轉換+聚合：生成器表達式（1.19）
# 展示如何使用生成器表達式進行轉換和聚合操作

# 數字列表
nums = [1, 2, 3]
# 計算所有數字的平方和：使用生成器表達式轉換，sum() 進行聚合
print("數字平方和:", sum(x * x for x in nums))  # 結果：14（1^2 + 2^2 + 3^2）

# 含有多種類型值的元組
s = ('ACME', 50, 123.45)
# 將元組中所有元素轉換為字串，並用逗號連接
print("元組轉字串:", ','.join(str(x) for x in s))  # 結果：'ACME,50,123.45'

# 投資組合列表：每個元素是字典，包含股票名稱和股數
portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]

# 方法 1：在生成器表達式中提取 shares，找最小值
print("最少股數:", min(s['shares'] for s in portfolio))  # 結果：20

# 方法 2：直接在列表上使用 min()，用 key 函數指定比較欄位
print("最少股數的投資:", min(portfolio, key=lambda s: s['shares']))  # 結果：{'name': 'AOL', 'shares': 20}
