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
print("--- 第一次存取 min(z) ---")
try:
    min_val = min(z)
    print(f"最小值是: {min_val}")
except ValueError as e:
    print(f"錯誤: {e}")

# 2. 第二次存取：慘劇發生
print("\n--- 第二次存取 max(z) ---")
try:
    # 此時 z 已經空了，min/max 對空序列會拋出 ValueError
    max_val = max(z)
    print(f"最大值是: {max_val}")
except ValueError:
    print("錯誤：ValueError: max() arg is an empty sequence")
    print("原因：zip 物件是一次性迭代器，已經被 min() 消耗殆盡了！")

# 若要同時取得 min/max，可先轉成 list：
# pairs = list(zip(prices.values(), prices.keys()))
# min(pairs)
# max(pairs)
