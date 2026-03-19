# R9. 兩字典相同點：keys/items 集合運算（1.9）

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 兩字典的 key 交集（共同擁有的 key）
a.keys() & b.keys()      # → {'x', 'y'}

# a 有但 b 沒有的 key（差集）
a.keys() - b.keys()      # → {'z'}

# items() 也能做集合運算，找出 key + value 都相同的項目
a.items() & b.items()    # → {('y', 2)}

# 用集合運算來挑出想保留的 key
# a.keys() - {'z', 'w'} = {'x', 'y'}
# 因此只會保留 x 和 y
c = {k: a[k] for k in a.keys() - {'z', 'w'}}