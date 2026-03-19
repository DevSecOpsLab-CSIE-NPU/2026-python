"""R17. 字典子集（1.17）

示範如何使用 dict comprehension 依條件建立字典子集。
"""

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# p1：過濾出價格大於 200 的項目，結果為新的字典
p1 = {k: v for k, v in prices.items() if v > 200}

tech_names = {'AAPL', 'IBM'}

# p2：僅保留 key 在 tech_names 集合內的項目 
p2 = {k: v for k, v in prices.items() if k in tech_names}
