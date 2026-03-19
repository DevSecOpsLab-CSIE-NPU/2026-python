"""R09: 字典的集合運算(keys/items)。"""

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

print('共同 keys:', a.keys() & b.keys())
print('a 獨有 keys:', a.keys() - b.keys())
print('共同 items:', a.items() & b.items())

# 字典推導式：排除特定 key
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
print('過濾後的 c:', c)
