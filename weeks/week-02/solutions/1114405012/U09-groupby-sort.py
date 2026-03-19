# U9. groupby 為何一定要先 sort（1.15）
#
# 觀念重點：groupby 不是「全域聚合」，它只會合併「連續出現」的同 key 資料。

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# 沒排序：07/02 會被切成前後兩段，因為中間插了一筆 07/01。
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)

# 先排序後，相同 date 會相鄰，groupby 才能得到正確分組。
rows.sort(key=itemgetter('date'))
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)
