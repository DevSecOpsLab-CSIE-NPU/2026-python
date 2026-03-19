"""
U09: groupby 之前要先排序

如果相同 key 沒排在一起，groupby 會把它們分成多組。
"""

from itertools import groupby
from operator import itemgetter


rows = [
    {"date": "07/02/2012", "x": 1},
    {"date": "07/01/2012", "x": 2},
    {"date": "07/02/2012", "x": 3},
]

# 沒排序時，兩筆 07/02/2012 不會被視為同一組。
for k, g in groupby(rows, key=itemgetter("date")):
    list(g)

# 先排序後，相同日期才會排在一起。
rows.sort(key=itemgetter("date"))
for k, g in groupby(rows, key=itemgetter("date")):
    list(g)
