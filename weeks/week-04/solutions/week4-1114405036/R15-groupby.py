# R15. 分組 groupby（1.15）
# 說明：利用 itertools.groupby 根據指定的 key 對資料進行分組。
# 注意：使用 groupby 之前，資料必須先根據該 key 進行排序 (Sort)，否則分組會出錯。

from itertools import groupby
from operator import itemgetter

# 模擬資料：一組包含日期與地址的字典
rows = [
    {'date': '07/01/2012', 'address': '5412 N CLARK ST'},
    {'date': '07/04/2012', 'address': '4801 N BROADWAY'},
    {'date': '07/01/2012', 'address': '1039 W GRANVILLE AVE'},
    {'date': '07/02/2012', 'address': '1060 W ADDISON ST'},
]

# 步驟 1：先根據 'date' 排序
# groupby 只會檢查相鄰的元素是否相同，所以必須先排序
rows.sort(key=itemgetter('date'))

# 步驟 2：進行分組
# groupby 會回傳 (key, iterable_of_items)
for date, items in groupby(rows, key=itemgetter('date')):
    print(f"日期: {date}")
    for i in items:
        print(f"  - 地址: {i['address']}")