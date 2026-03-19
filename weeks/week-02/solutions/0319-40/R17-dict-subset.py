# R17. 字典子集（1.17）

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 用字典推導式建立子集：只保留價格大於 200 的項目
price_over_200 = {k: v for k, v in prices.items() if v > 200}

tech_names = {'AAPL', 'IBM'}

# 只保留 key 在指定集合中的項目
tech_prices = {k: v for k, v in prices.items() if k in tech_names}
