# R9. 兩字典相同點：keys/items 集合運算（1.9）
# dictionary views behave like集合，因此可進行集合運算。

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

print("a keys & b keys", a.keys() & b.keys())
print("a keys - b keys", a.keys() - b.keys())
print("a items & b items", a.items() & b.items())

c = {k: a[k] for k in a.keys() - {'z', 'w'}}
print("filter out z,w ->", c)
