"""
R09: 字典視圖的集合運算

dict_keys 與 dict_items 支援集合交集/差集等操作。
"""

a = {"x": 1, "y": 2, "z": 3}
b = {"w": 10, "x": 11, "y": 2}

# 共同鍵（交集）。
a.keys() & b.keys()

# a 有、b 沒有的鍵（差集）。
a.keys() - b.keys()

# 完全相同的 (key, value) 配對交集。
a.items() & b.items()

# 字典推導式：從 a 複製資料，但排除指定鍵。
c = {k: a[k] for k in a.keys() - {"z", "w"}}
