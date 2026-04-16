# R9. 兩字典相同點：keys/items 集合運算（1.9）
#
# 字典的 keys() 和 items() 都可以像集合一樣做運算：
# 1. 交集 &：找出兩個字典共同擁有的 key 或 key/value。
# 2. 差集 -：找出某個字典有、另一個沒有的 key。
# 3. 這種寫法很適合比對兩份資料之間的差異。

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

a.keys() & b.keys()
a.keys() - b.keys()
a.items() & b.items()

c = {k: a[k] for k in a.keys() - {'z', 'w'}}
