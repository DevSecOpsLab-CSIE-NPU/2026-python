# R17. 字典子集（1.17）

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 取出 value > 200 的子字典
p1 = {k: v for k, v in prices.items() if v > 200}
# → {'AAPL': 612.78, 'IBM': 205.55}

# 取出 key 在指定集合中的子字典
tech_names = {'AAPL', 'IBM'}
p2 = {k: v for k, v in prices.items() if k in tech_names}
# → {'AAPL': 612.78, 'IBM': 205.55}