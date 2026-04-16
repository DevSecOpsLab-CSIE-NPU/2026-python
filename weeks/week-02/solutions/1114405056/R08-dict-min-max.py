# R8. 字典運算：min/max/sorted + zip（1.8）

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))
sorted(zip(prices.values(), prices.keys()))

min(prices, key=lambda k: prices[k])  # 回傳 key
