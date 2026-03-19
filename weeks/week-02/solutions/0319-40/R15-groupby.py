# R15. 分組 groupby（1.15）

from itertools import groupby
from operator import itemgetter

# 原始資料：每筆資料都有日期和地址
rows = [
    {'date': '07/01/2012', 'address': '...'},
    {'date': '07/02/2012', 'address': '...'},
]

# groupby 只會把「連續且 key 相同」的資料分在一起，
# 所以實務上通常要先依 key 排序。
rows.sort(key=itemgetter('date'))

# 依 date 分組，date 是分組鍵，items 是同日期的一組迭代器
for date, items in groupby(rows, key=itemgetter('date')):
    # 逐筆處理該日期底下的資料
    for item in items:
        # 這裡可改成 print(item) 或其他商業邏輯
        pass
