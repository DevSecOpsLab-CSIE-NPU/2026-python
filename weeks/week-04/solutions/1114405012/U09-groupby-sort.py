# U9. groupby 為何一定要先 sort（1.15）
# groupby 的行為是「相鄰相同就分同組」，不是全域掃描。

from itertools import groupby
from operator import itemgetter

rows = [
    {"date": "07/02/2012", "x": 1},
    {"date": "07/01/2012", "x": 2},
    {"date": "07/02/2012", "x": 3},
    {"date": "07/01/2012", "x": 4},
]

print("=== 未排序直接 groupby ===")
for k, g in groupby(rows, key=itemgetter("date")):
    group = list(g)
    print(k, "->", group)

# 先排序後，同日期元素才會連續。
rows.sort(key=itemgetter("date"))
print("\n=== 先排序再 groupby ===")
for k, g in groupby(rows, key=itemgetter("date")):
    group = list(g)
    print(k, "->", group)
