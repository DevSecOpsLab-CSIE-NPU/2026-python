# R19. 轉換+聚合：生成器表達式（1.19）
"""
本範例示範如何在聚合運算（如 sum、min）中使用生成器表達式（generator expression）進行資料轉換。

生成器表達式的特性：
- 產生器是一次性可迭代的，不會一次性建立整個中間列表，節省記憶體
- 可以直接嵌入到聚合函式中，語法簡潔明瞭

常見用途：
- 大量資料運算（例如累加、求最大/最小值）
- 將資料轉換成另一種形式後再聚合（如求平方和、字串連接）
"""

# 範例 1：對數字列表進行平方後求和
nums = [1, 2, 3]

# sum(x * x for x in nums)：直接使用生成器表達式計算平方，並進行加總
# 這裡沒有建立中間列表，效率更好
sum(x * x for x in nums)

# 範例 2：將不同型別的元素轉為字串，並用逗號連接
s = ('ACME', 50, 123.45)

# 生成器表達式 str(x) for x in s 會逐一將元素轉為字串
# 透過 ','.join(...) 將所有字串以逗號連接起來
','.join(str(x) for x in s)

# 範例 3：從投資組合中計算最小的持股數
portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]

# 方法 1：使用生成器表達式取得每個持股數，然後求最小值
min(s['shares'] for s in portfolio)

# 方法 2：使用 min 的 key 參數直接對字典進行比較（更 Pythonic）
min(portfolio, key=lambda s: s['shares'])
