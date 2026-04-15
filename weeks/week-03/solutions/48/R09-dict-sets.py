# R9. 兩字典相同點：keys/items 集合運算（1.9）

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 共同 key（交集）
a.keys() & b.keys()
# 只在 a 出現的 key（差集）
a.keys() - b.keys()
# 完全相同的 (key, value) 配對
a.items() & b.items()

# 字典推導式：排除指定 key 建立新字典
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
