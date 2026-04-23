# 【Bloom 階段：R - 記憶與基本操作】
# R8. 字典運算：最小值、最大值與排序
# August 的惡意提醒：直接對字典做 min() 會是在比 Key。
# 想要比 Value 且同時拿到 Key？用 zip(values, keys) 是最聰明的「找碴」解法。

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# 1. 技巧一：利用 zip 將 (值, 鍵) 配對，min/max 就會以「值」為基準
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
sorted_prices = sorted(zip(prices.values(), prices.keys()))

# 2. 技巧二：使用 min() 的 key 參數 (只會拿回 Key)
min_key = min(prices, key=lambda k: prices[k])

print(f"Min Price: {min_price}")
print(f"Sorted by price: {sorted_prices}")
# August 惡意筆記：zip 產生的迭代器只能走一次，記住 Week 01 主題 06 的教訓！
