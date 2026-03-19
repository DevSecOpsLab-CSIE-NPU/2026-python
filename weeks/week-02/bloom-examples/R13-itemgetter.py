"""R13: itemgetter 用於 dict/list 排序。"""

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
]

print('依 fname 排序:', sorted(rows, key=itemgetter('fname')))
print('依 uid 排序:', sorted(rows, key=itemgetter('uid')))
print('依 uid, fname 排序:', sorted(rows, key=itemgetter('uid', 'fname')))
