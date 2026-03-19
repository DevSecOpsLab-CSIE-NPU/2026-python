# U10. zip 為何只能用一次（1.8）

prices = {'A': 2.0, 'B': 1.0}
z = zip(prices.values(), prices.keys())

min(z)  # OK（消耗掉迭代器）
# max(z)  # 會失敗：因為 z 已經被消耗完
