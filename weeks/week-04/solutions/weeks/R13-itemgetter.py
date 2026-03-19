# R13. 字典列表排序 itemgetter（1.13）

from operator import itemgetter

# 一個由字典組成的列表
rows = [
    {'fname': 'Brian', 'uid': 1003},
    {'fname': 'John',  'uid': 1001}
]

# 依照字典中的 'fname' 欄位排序
sorted(rows, key=itemgetter('fname'))
# → [{'fname': 'Brian', ...}, {'fname': 'John', ...}]

# 依照 'uid' 欄位排序（數字排序）
sorted(rows, key=itemgetter('uid'))
# → [{'fname': 'John', 'uid': 1001}, {'fname': 'Brian', 'uid': 1003}]

# 同時依照多個欄位排序：先依 'uid'，再依 'fname'
sorted(rows, key=itemgetter('uid', 'fname'))