# R09 dict sets
# 目標：示範兩個字典在 keys/items 上的集合運算。

a = {"x": 1, "y": 2, "z": 3}
b = {"w": 10, "x": 11, "y": 2}

# 共同 key
common_keys = a.keys() & b.keys()
# a 有、b 沒有的 key
only_in_a = a.keys() - b.keys()
# 共同 (key, value) 配對
common_items = a.items() & b.items()

# 字典推導：排除不需要的 key
c = {k: a[k] for k in a.keys() - {"z", "w"}}
