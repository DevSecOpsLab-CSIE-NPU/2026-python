# R13: itemgetter
# 觀念：itemgetter 會回傳一個可取欄位值的函式，常用在 sorted(key=...)。

from operator import itemgetter

rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]

# 依 fname 排序
sorted(rows, key=itemgetter('fname'))

# 依 uid 排序
sorted(rows, key=itemgetter('uid'))

# 多鍵排序：先 uid，再 fname
sorted(rows, key=itemgetter('uid', 'fname'))
