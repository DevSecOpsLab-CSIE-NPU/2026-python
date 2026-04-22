# U10. zip 為何只能用一次（1.8）
# zip 回傳的是「迭代器」，元素被取走後就不會自動回來。

prices = {"A": 2.0, "B": 1.0, "C": 3.5}
z = zip(prices.values(), prices.keys())

print("第一次 min(z):", min(z))

# 第二次再用同一個 z，會因為已被消耗而沒有元素。
try:
    print("第二次 max(z):", max(z))
except ValueError as e:
    print("max(z) 失敗:", e)

# 正確做法 1：每次重新建立 zip
print("重新建立後 max:", max(zip(prices.values(), prices.keys())))

# 正確做法 2：先轉 list（可重複使用，但會多耗記憶體）
pairs = list(zip(prices.values(), prices.keys()))
print("pairs:", pairs)
print("list 版 min:", min(pairs))
print("list 版 max:", max(pairs))
