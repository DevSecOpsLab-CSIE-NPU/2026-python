# U10 zip 產生的是一次性迭代器
# 重點：迭代器被消耗後不能重複使用。

prices = {"A": 2.0, "B": 1.0}
z = zip(prices.values(), prices.keys())

# 第一次消耗 z 成功。
min(z)

# 第二次再用 z 會失敗，因為 z 已被前一次操作消耗完。
# max(z)
