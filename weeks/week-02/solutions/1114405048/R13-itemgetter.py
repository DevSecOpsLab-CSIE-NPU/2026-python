# R13 itemgetter
# 目標：對字典列表依欄位排序。

from operator import itemgetter

rows = [{"fname": "Brian", "uid": 1003}, {"fname": "John", "uid": 1001}]

by_fname = sorted(rows, key=itemgetter("fname"))
by_uid = sorted(rows, key=itemgetter("uid"))
by_uid_fname = sorted(rows, key=itemgetter("uid", "fname"))
