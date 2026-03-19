# U10. zip 為何只能用一次（1.8）
#
# 觀念重點：
# - zip 在 Python 3 回傳的是 iterator（惰性序列）。
# - iterator 被迭代後就會前進，元素不會自動重置。

prices = {'A': 2.0, 'B': 1.0}
z = zip(prices.values(), prices.keys())

# 第一次使用 z，會把資料逐步取出直到耗盡。
min(z)

# 再次使用同一個 z 時已沒有元素可讀。
# max(z)  # ValueError: max() arg is an empty sequence

# 若要重用，需重新建立 iterator：
# z = zip(prices.values(), prices.keys())
