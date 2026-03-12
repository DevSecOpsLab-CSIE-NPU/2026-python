# R9: 字典的集合運算
# 觀念：dict 的 keys()/items() 檢視物件可做集合交集、差集等運算。

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 共同 key
a.keys() & b.keys()

# 在 a 裡但不在 b 的 key
a.keys() - b.keys()

# 共同的 (key, value) 配對
a.items() & b.items()

# 字典推導：排除指定 key 後建立新字典
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
