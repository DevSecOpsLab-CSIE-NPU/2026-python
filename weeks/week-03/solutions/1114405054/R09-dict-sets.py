# R9. 兩字典相同點：keys/items 集合運算（1.9）

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

a.keys() & b.keys()
a.keys() - b.keys()
a.items() & b.items()

c = {k: a[k] for k in a.keys() - {'z', 'w'}}
