# R8. 字典運算：min/max/sorted + zip（1.8）

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# zip(value, key) 後可直接比較 value，結果會回傳 (value, key)
min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))
sorted(zip(prices.values(), prices.keys()))

# 也可用 key 參數，回傳最小值對應的 key
min(prices, key=lambda k: prices[k])  # 回傳 key
