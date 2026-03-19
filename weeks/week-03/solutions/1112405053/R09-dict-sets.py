# R9. 兩字典相同點：keys/items 集合運算（1.9）

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 共同 key
a.keys() & b.keys()
# a 有、b 沒有的 key
a.keys() - b.keys()
# 完全相同的 (key, value)
a.items() & b.items()

# 字典推導：排除指定 key 後建立新字典
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
