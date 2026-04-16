# R13. 字典列表排序 itemgetter（1.13）

from operator import itemgetter

rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]
sorted(rows, key=itemgetter('fname'))
sorted(rows, key=itemgetter('uid'))
sorted(rows, key=itemgetter('uid', 'fname'))
