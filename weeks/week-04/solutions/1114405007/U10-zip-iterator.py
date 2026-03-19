# U10. zip 為何只能用一次（1.8）

prices = {'A': 2.0, 'B': 1.0}

# zip 回傳的是迭代器，不是可重複使用的串列
z = zip(prices.values(), prices.keys())

first = min(z)  # OK（消耗掉迭代器）

# max(z)  # 會失敗：因為 z 已經被消耗完
print('第一次 min(z) =', first)

try:
	print('第二次 max(z) =', max(z))
except ValueError as error:
	print('第二次使用失敗:', error)
