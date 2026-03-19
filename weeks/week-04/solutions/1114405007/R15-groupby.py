# R15. 分組 groupby（1.15）

from itertools import groupby
from operator import itemgetter

# 範例資料：每筆資料都有日期與地址欄位
rows = [{'date': '07/01/2012', 'address': '...'}, {'date': '07/02/2012', 'address': '...'}]

# groupby 只會把連續且鍵值相同的資料分在一起，因此通常要先排序
rows.sort(key=itemgetter('date'))

# 依照 date 欄位分組，date 是分組鍵，items 是該組的所有資料
for date, items in groupby(rows, key=itemgetter('date')):
    # 逐筆處理同一個日期底下的資料
    for i in items:
        pass
