# R13. 字典列表排序 itemgetter（1.13）

from operator import itemgetter

rows = [
	{'fname': 'Brian', 'uid': 1003},
	{'fname': 'John', 'uid': 1001},
	{'fname': 'Alice', 'uid': 1001},
]

# 依名字排序
by_fname = sorted(rows, key=itemgetter('fname'))
# 依 uid 排序
by_uid = sorted(rows, key=itemgetter('uid'))
# 先 uid、再 fname（多鍵排序）
by_uid_fname = sorted(rows, key=itemgetter('uid', 'fname'))

print('原始 rows:', rows)
print('依 fname 排序:', by_fname)
print('依 uid 排序:', by_uid)
print('依 uid, fname 排序:', by_uid_fname)
