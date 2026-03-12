"""
R08: 字典的最值查找

示範 min/max/sorted 搭配 zip，與 key 參數的用法。
"""

prices = {"ACME": 45.23, "AAPL": 612.78, "FB": 10.75}

# zip(value, key) 後，可直接比較價格，再取出對應股票代號。
min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))
sorted(zip(prices.values(), prices.keys()))

# 另一種寫法：直接在鍵集合上做 min，並用 key 指定比較依據是 prices[k]。
min(prices, key=lambda k: prices[k])
