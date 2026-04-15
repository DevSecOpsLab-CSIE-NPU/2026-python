# R8. 字典運算：min/max/sorted + zip（1.8）

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# zip(value, key) 之後，min/max 會先按 value 比較
min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))
# 排序後可得到由小到大的 (value, key) 清單
sorted(zip(prices.values(), prices.keys()))

# 直接對 key 做 min，透過 key 函式改成比較對應 value
min(prices, key=lambda k: prices[k])  # 回傳 key
