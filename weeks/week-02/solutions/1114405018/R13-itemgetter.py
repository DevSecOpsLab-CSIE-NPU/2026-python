"""R13. 字典列表排序 itemgetter（1.13）

itemgetter() 常用於 sorted / min / max 等函式的 key 參數。
它可以很方便地從字典或序列中取出指定欄位，作為排序依據。
"""

from operator import itemgetter

# rows 是一個字典列表，每個字典都有 fname 與 uid
rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]

# 依 fname 欄位排序
sorted(rows, key=itemgetter('fname'))

# 依 uid 欄位排序
sorted(rows, key=itemgetter('uid'))

# 先比 uid，再比 fname（多欄位排序）
sorted(rows, key=itemgetter('uid', 'fname'))
