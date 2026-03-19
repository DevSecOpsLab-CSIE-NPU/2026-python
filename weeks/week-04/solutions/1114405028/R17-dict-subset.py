# R17. 字典子集（1.17）

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 字典推導式：只保留 value > 200 的項目
p1 = {k: v for k, v in prices.items() if v > 200}
# 結果：{'AAPL': 612.78, 'IBM': 205.55}

tech_names = {'AAPL', 'IBM'}  # 用集合存放白名單股票代號，查詢效率 O(1)

# 字典推導式：只保留 key 在 tech_names 集合中的項目
p2 = {k: v for k, v in prices.items() if k in tech_names}
# 結果：{'AAPL': 612.78, 'IBM': 205.55}
