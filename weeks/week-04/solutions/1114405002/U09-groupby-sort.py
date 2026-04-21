# U09 groupby 之前通常要先排序
# 重點：groupby 只會合併連續區段，不會自動把同 key 分散項目聚在一起。

from itertools import groupby
from operator import itemgetter

rows = [
    {"date": "07/02/2012", "x": 1},
    {"date": "07/01/2012", "x": 2},
    {"date": "07/02/2012", "x": 3},
]

# 未排序時，相同日期可能被拆成多段群組。
for k, g in groupby(rows, key=itemgetter("date")):
    list(g)

# 先排序後再 groupby，才能把相同日期完整聚合。
rows.sort(key=itemgetter("date"))
for k, g in groupby(rows, key=itemgetter("date")):
    list(g)
