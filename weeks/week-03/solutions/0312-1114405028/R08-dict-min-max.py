# R8. 字典運算：min/max/sorted + zip（1.8）
# zip 可將值與鍵配對，便於求最小/最大。

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}
print("prices", prices)
print("最低價對 ->", min(zip(prices.values(), prices.keys())))
print("最高價對 ->", max(zip(prices.values(), prices.keys())))
print("排序後列表 ->", sorted(zip(prices.values(), prices.keys())))

print("直接用 key 函數求最低價股票 ->", min(prices, key=lambda k: prices[k]))
