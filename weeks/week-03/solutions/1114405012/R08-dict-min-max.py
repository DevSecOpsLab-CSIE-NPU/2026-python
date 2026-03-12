# R8. 字典運算：min/max/sorted + zip（1.8）

# 建立商品與價格字典
prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# zip(價格, 名稱) 後可直接做比較與排序
min_pair = min(zip(prices.values(), prices.keys()))
max_pair = max(zip(prices.values(), prices.keys()))
sorted_pairs = sorted(zip(prices.values(), prices.keys()))
print('最低價格 (價格, 名稱):', min_pair)
print('最高價格 (價格, 名稱):', max_pair)
print('依價格排序:', sorted_pairs)

# 直接找價格最低商品名稱（回傳 key）
cheapest_name = min(prices, key=lambda k: prices[k])
print('最便宜商品名稱:', cheapest_name)
