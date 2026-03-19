# R15. 分組 groupby（1.15）

from itertools import groupby
from operator import itemgetter

# 一個字典列表，每筆資料都有 date 欄位
rows = [
    {'date': '07/01/2012', 'address': '...'},
    {'date': '07/02/2012', 'address': '...'}
]

# groupby 要求資料必須先依分組 key 排序
rows.sort(key=itemgetter('date'))

# groupby(rows, key=itemgetter('date')) 會依 date 分組
# 每次迭代會回傳：
#   date  → 分組的 key
#   items → 該組內的所有元素（是一個 iterator）
for date, items in groupby(rows, key=itemgetter('date')):
    for i in items:
        pass   # 在這裡處理每一筆資料