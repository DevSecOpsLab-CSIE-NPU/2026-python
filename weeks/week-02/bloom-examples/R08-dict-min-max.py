"""R08: 字典最小值/最大值與 zip 技巧。"""

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# 用 zip 產生 (value, key) 方便同時拿到值與名稱
print('最便宜:', min(zip(prices.values(), prices.keys())))
print('最貴:', max(zip(prices.values(), prices.keys())))
print('依價格排序:', sorted(zip(prices.values(), prices.keys())))

# 用 key 參數只取 key（公司名）
print('最便宜公司:', min(prices, key=lambda k: prices[k]))
print('最貴公司:', max(prices, key=lambda k: prices[k]))
