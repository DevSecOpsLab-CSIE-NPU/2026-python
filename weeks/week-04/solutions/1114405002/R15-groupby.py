# R15 itertools.groupby 範例
# 重點：groupby 只會把「相鄰且 key 相同」的項目分在同一組，通常要先排序。

from itertools import groupby
from operator import itemgetter

rows = [
    {"date": "07/01/2012", "address": "..."},
    {"date": "07/02/2012", "address": "..."},
]

# 先依 date 排序，確保同日期資料相鄰。
rows.sort(key=itemgetter("date"))

for date, items in groupby(rows, key=itemgetter("date")):
    # items 是同日期的一個迭代器群組。
    for item in items:
        pass
