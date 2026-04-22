# U8. 字典最值為何常用 zip(values, keys)（1.8）
# 目標：同時拿到「最值」與其對應的 key。

prices = {"A": 2.0, "B": 1.0, "C": 3.5}

# 直接對 dict 做 min/max，實際上比較的是 key。
print("min(prices) ->", min(prices))
print("max(prices) ->", max(prices))

# 對 values 做 min/max，只有數值本身，會失去 key 資訊。
print("min(prices.values()) ->", min(prices.values()))
print("max(prices.values()) ->", max(prices.values()))

# 用 zip(value, key) 後比較時先比 value，可同時保留 key。
min_pair = min(zip(prices.values(), prices.keys()))
max_pair = max(zip(prices.values(), prices.keys()))
print("最小 (value, key):", min_pair)
print("最大 (value, key):", max_pair)
