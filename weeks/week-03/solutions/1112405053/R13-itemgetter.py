# R13. 字典列表排序 itemgetter（1.13）

from operator import itemgetter

rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]
# 依 fname 排序
sorted(rows, key=itemgetter('fname'))
# 依 uid 排序
sorted(rows, key=itemgetter('uid'))
# 先比 uid，再比 fname
sorted(rows, key=itemgetter('uid', 'fname'))
