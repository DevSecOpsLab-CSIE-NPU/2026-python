# R15. 分組 groupby（1.15）
# 重點：groupby 只會把「連續且 key 相同」的資料分在一起，所以通常要先排序。

from itertools import groupby
from operator import itemgetter

rows = [
    {"date": "07/01/2012", "address": "5412 N CLARK"},
    {"date": "07/01/2012", "address": "4801 N BROADWAY"},
    {"date": "07/02/2012", "address": "5800 E 58TH"},
    {"date": "07/03/2012", "address": "2122 N CLARK"},
    {"date": "07/02/2012", "address": "5645 N RAVENSWOOD"},
]

# 先依 date 排序，確保相同日期資料相鄰。
rows.sort(key=itemgetter("date"))

print("=== groupby 分組結果 ===")
for date, items in groupby(rows, key=itemgetter("date")):
    # group 會是同一日期的迭代器，通常先轉成 list 方便後續使用。
    group = list(items)
    print(f"日期 {date} 共 {len(group)} 筆:")
    for item in group:
        print(f"  - {item['address']}")
