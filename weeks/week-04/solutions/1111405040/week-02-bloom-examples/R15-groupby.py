"""
R15: groupby

示範如何依某個欄位分組。
"""

from itertools import groupby
from operator import itemgetter


rows = [
    {"date": "07/01/2012", "address": "..."},
    {"date": "07/02/2012", "address": "..."},
]

# groupby 只會把「連在一起」的相同 key 視為同一組，
# 所以通常要先依同一個 key 排序。
rows.sort(key=itemgetter("date"))

for date, items in groupby(rows, key=itemgetter("date")):
    for item in items:
        pass
