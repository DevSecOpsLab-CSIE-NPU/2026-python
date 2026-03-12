# R9. 兩字典相同點：keys/items 集合運算（1.9）

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 找共同 key、只在 a 的 key、共同 (key, value)
common_keys = a.keys() & b.keys()
only_in_a = a.keys() - b.keys()
common_items = a.items() & b.items()
print('共同 keys:', common_keys)
print('只在 a 的 keys:', only_in_a)
print('共同 items:', common_items)

# 字典推導式：移除不想要的 key
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
print('過濾後字典 c:', c)
