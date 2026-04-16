"""R8. 字典運算：min / max / sorted + zip（1.8）

這個範例示範如何從字典中找出：
1. 最小值 / 最大值對應的項目
2. 依照值排序所有項目
3. 直接用 key 參數找出字典中最小的 key
"""

# 字典：key 是股票代號，value 是價格
prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# zip(prices.values(), prices.keys()) 會把「值」和「鍵」配成 (value, key)
# 這樣 min / max / sorted 就會優先比較 value
min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))
sorted(zip(prices.values(), prices.keys()))

# 也可以直接對字典的 key 做 min / max，然後用 key=lambda k: prices[k]
# 告訴 Python：比較時要看該 key 對應的價格
min(prices, key=lambda k: prices[k])  # 回傳 key
