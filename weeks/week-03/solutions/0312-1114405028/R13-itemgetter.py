# R13. 字典列表排序 itemgetter（1.13）
# itemgetter 從 dict 或 tuple 中取得項目作為排序鍵。

from operator import itemgetter

rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]
print("original rows", rows)
print("sort by fname", sorted(rows, key=itemgetter('fname')))
print("sort by uid", sorted(rows, key=itemgetter('uid')))
print("sort by uid then fname", sorted(rows, key=itemgetter('uid', 'fname')))

