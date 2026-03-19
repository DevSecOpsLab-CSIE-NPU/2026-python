# R17. 字典子集（1.17）

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 透過字典推導式，挑出價格大於 200 的項目
p1 = {k: v for k, v in prices.items() if v > 200}

tech_names = {'AAPL', 'IBM'}

# 只保留鍵在指定集合中的項目
p2 = {k: v for k, v in prices.items() if k in tech_names}
