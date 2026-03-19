# R8. 字典運算：min/max/sorted + zip（1.8）

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# zip(prices.values(), prices.keys()) 會產生 (value, key) 的配對
# min() 會依照 value（價格）找出最小的那組
min(zip(prices.values(), prices.keys()))     # → (10.75, 'FB')

# max() 同理，找出價格最高的那組
max(zip(prices.values(), prices.keys()))     # → (612.78, 'AAPL')

# sorted() 會依照 value 排序所有 (value, key) 配對
sorted(zip(prices.values(), prices.keys()))
# → [(10.75, 'FB'), (45.23, 'ACME'), (612.78, 'AAPL')]

# 直接用 min() 找出價格最低的 key
# key 參數指定比較依據：prices[k]
min(prices, key=lambda k: prices[k])         # → 'FB'