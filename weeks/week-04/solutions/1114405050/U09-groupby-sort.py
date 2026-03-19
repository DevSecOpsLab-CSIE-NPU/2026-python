# U9. groupby 為何一定要先 sort（1.15）
"""
本範例示範為什麼使用 itertools.groupby 時，必須先對資料進行排序。

itertools.groupby 只會把「連續出現」的相同 key 合併成一組，
若資料中相同 key 的項目分散出現（沒有排序），則會被拆成多個分組。

因此在使用 groupby 前一定要先根據相同的 key 做排序，
才能保證分組結果是符合預期的。
"""

from itertools import groupby
from operator import itemgetter

# 範例資料：三筆字典，其中 date 欄位有重複值
rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# 直接呼叫 groupby（未排序）
# groupby 只會將連續相同 key 的項目視為一組
# 因此這裡會先分到 07/02 再到 07/01 再回到 07/02，
# 導致 07/02 被拆成兩個分組，結果不正確。
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)

# 正確做法：先排序，讓相同 date 的資料連在一起
rows.sort(key=itemgetter('date'))

# 排序後再次 groupby，就會得到「按 date 分組」的正確結果
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)
