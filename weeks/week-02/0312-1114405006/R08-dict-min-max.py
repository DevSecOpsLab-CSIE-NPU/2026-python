# R8. 字典運算：min/max/sorted + zip（1.8）
#
# 這個範例示範如何同時比較 key 與 value：
# 1. zip(prices.values(), prices.keys()) 會把價格和商品名稱配對。
# 2. min / max / sorted 可以直接對配對後的資料做排序或取極值。
# 3. 若只想知道最便宜或最貴的商品，也可以直接用 key 參數。

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))
sorted(zip(prices.values(), prices.keys()))

min(prices, key=lambda k: prices[k])  # 回傳 key
