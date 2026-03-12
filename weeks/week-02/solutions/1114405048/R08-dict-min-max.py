# R08 dict min/max
# 目標：示範字典值比較與排序技巧。

prices = {"ACME": 45.23, "AAPL": 612.78, "FB": 10.75}

# zip(value, key) 後，min/max 會先比 value
min_pair = min(zip(prices.values(), prices.keys()))
max_pair = max(zip(prices.values(), prices.keys()))
sorted_pairs = sorted(zip(prices.values(), prices.keys()))

# 直接找最小價格的公司 key
min_key = min(prices, key=lambda k: prices[k])
