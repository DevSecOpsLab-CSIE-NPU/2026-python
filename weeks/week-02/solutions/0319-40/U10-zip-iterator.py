# U10. zip 為何只能用一次（1.8）

prices = {'A': 2.0, 'B': 1.0}
z = zip(prices.values(), prices.keys())

first = min(z)  # 第一次使用，會消耗迭代器
print('第一次 min(z) =', first)

# 第二次再用同一個 z，會沒有資料
try:
    second = max(z)
    print('第二次 max(z) =', second)
except ValueError as err:
    print('第二次 max(z) 失敗：', err)

# 正確做法：重建 zip
z2 = zip(prices.values(), prices.keys())
print('重建後 max(z2) =', max(z2))
