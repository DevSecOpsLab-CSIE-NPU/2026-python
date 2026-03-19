# R15. 分組 groupby（1.15）

from itertools import groupby    # groupby：將連續相同 key 的元素聚合成一組
from operator import itemgetter  # itemgetter：快速取出 dict/tuple 中指定欄位，比 lambda 效率稍高

rows = [{'date': '07/01/2012', 'address': '...'}, {'date': '07/02/2012', 'address': '...'}]
rows.sort(key=itemgetter('date'))  # 必須先排序！groupby 只對「連續相同」的 key 分組
                                   # 若不排序，相同日期若不相鄰會被分成多組

for date, items in groupby(rows, key=itemgetter('date')):
    # date：目前分組的鍵值（日期字串）
    # items：屬於該日期的所有資料（惰性迭代器，只能讀一次）
    for i in items:
        pass  # 在這裡處理每筆同日期的資料
