# R8: 字典的最小值/最大值與排序
# 觀念：常見需求是「依 value 找 key」，可用 zip(value, key) 技巧。

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# zip(prices.values(), prices.keys()) 產生 (value, key) 配對
# min/max 會先比 value，再比 key（若 value 相同）
min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))
sorted(zip(prices.values(), prices.keys()))

# 另一種直觀寫法：直接在 key 上用 lambda 指定比較依據是 prices[k]
min(prices, key=lambda k: prices[k])
