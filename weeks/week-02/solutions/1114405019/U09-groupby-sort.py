# U9. groupby 為何一定要先 sort（1.15）

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# 沒排序：07/02 會被分成兩段（因為 groupby 只看「連續」）
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)

# 排序後：同 date 才會連在一起，分組才正確
rows.sort(key=itemgetter('date'))
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)
