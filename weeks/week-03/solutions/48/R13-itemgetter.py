# R13. 字典列表排序 itemgetter（1.13）

from operator import itemgetter

rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]
# 依單一欄位 fname 排序
sorted(rows, key=itemgetter('fname'))
# 依單一欄位 uid 排序
sorted(rows, key=itemgetter('uid'))
# 依多欄位排序：先 uid，再 fname
sorted(rows, key=itemgetter('uid', 'fname'))
