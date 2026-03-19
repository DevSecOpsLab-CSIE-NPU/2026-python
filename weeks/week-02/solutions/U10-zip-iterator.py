# U10. zip 為何只能用一次（1.8）
#
# Python 的 zip() 會回傳一個 iterator（惰性評估的物件），
# 它只會在「被消費」時才產生元素，而且一旦消費過就不會重置。
#
# 這和 list 不同：list 是可重複迭代的容器；
# iterator 則是「單次」的，走過一次就沒了。
#
# 因此同一個 zip 物件不能在不同的地方重複使用，
# 要重用結果就必須先把它轉成 list（或其他序列）。

prices = {'A': 2.0, 'B': 1.0}
z = zip(prices.values(), prices.keys())

min(z)  # OK（消耗掉迭代器）
# max(z)  # 會失敗：因為 z 已經被消耗完

# 若要同時取得 min/max，可先轉成 list：
# pairs = list(zip(prices.values(), prices.keys()))
# min(pairs)
# max(pairs)
