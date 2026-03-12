# R13. 字典列表排序 itemgetter（Sorting a List of Dictionaries by a Common Key）—— Python Cookbook 1.13

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'uid': 1003},
    {'fname': 'John',  'uid': 1001},
]

# ── itemgetter 作為 key 函式 ──────────────────────────────
# itemgetter('fname') 等同於 lambda d: d['fname']，
# 但比 lambda 稍快（C 層級實作，少了 Python 函式呼叫開銷）

# 依 fname 排序（字母順序）
sorted(rows, key=itemgetter('fname'))
# → [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]

# 依 uid 排序（數字大小）
sorted(rows, key=itemgetter('uid'))
# → [{'fname': 'John', 'uid': 1001}, {'fname': 'Brian', 'uid': 1003}]

# ── 多欄位排序 ────────────────────────────────────────────
# itemgetter('uid', 'fname') 先依 uid 排，uid 相同再依 fname 排
# 等同於 lambda d: (d['uid'], d['fname'])
sorted(rows, key=itemgetter('uid', 'fname'))

# ── 降序排列 ─────────────────────────────────────────────
# 加上 reverse=True 即可反轉排序結果
# sorted(rows, key=itemgetter('uid'), reverse=True)
