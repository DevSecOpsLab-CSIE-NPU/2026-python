# R15. 分組 groupby（1.15）
"""
本範例展示如何使用 itertools.groupby 依照指定欄位對資料進行分組。

重要觀念：
- groupby 只會對**連續相同 key 的項目**進行分組，因此在使用前必須先排序。
- groupby 產生的每一個分組是一個可迭代的 generator，一旦遍歷過就會耗盡。

應用場景：
- 依日期、類別、狀態等欄位分組資料
- 在分組後進行統計、累加或輸出報表
"""

from itertools import groupby
from operator import itemgetter

# 範例資料：每筆資料為 dict，包含日期與地址
rows = [
    {'date': '07/01/2012', 'address': '...'},
    {'date': '07/02/2012', 'address': '...'},
]

# 1) 必須先排序，排序 key 必須與 groupby 的 key 一致
#    否則相同的 key 會被分散到不同分組中
rows.sort(key=itemgetter('date'))

# 2) 使用 groupby 進行分組
#    其回傳值為 (key, group_iterator)
#    其中 group_iterator 為可迭代物件，遍歷後即消耗
for date, items in groupby(rows, key=itemgetter('date')):
    # items 為該日期的子集合，可進行累加、統計、輸出等操作
    for i in items:
        # 在此範例僅示意遍歷，實際可根據需求處理每筆資料
        pass
