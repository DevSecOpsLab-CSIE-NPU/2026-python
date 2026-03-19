"""U10: zip 是一次性迭代器，用過就沒了。"""

prices = {'A': 2.0, 'B': 1.0, 'C': 3.0}
z = zip(prices.values(), prices.keys())

print('第一次 min(z):', min(z))

# z 已經被消耗，轉 list 會是空的
print('第二次查看 z:', list(z))

# 要重用就重新建立一個 zip
z2 = zip(prices.values(), prices.keys())
print('重新建立後 max(z2):', max(z2))
