"""
R13: itemgetter

itemgetter 會回傳一個可呼叫物件，常用於排序 key。
"""

from operator import itemgetter

rows = [{"fname": "Brian", "uid": 1003}, {"fname": "John", "uid": 1001}]

# 依 fname 字母順序排序。
sorted(rows, key=itemgetter("fname"))

# 依 uid 數值排序。
sorted(rows, key=itemgetter("uid"))

# 多欄位排序：先比 uid，再比 fname。
sorted(rows, key=itemgetter("uid", "fname"))
