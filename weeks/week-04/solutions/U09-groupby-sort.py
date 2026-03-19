# U9. groupby 為何一定要先 sort（1.15）
#
# itertools.groupby 不是在整個序列中找到相同 key 的所有項目，
# 它只會把「連續」且 key 相同的項目歸類在一起。
#
# 因此如果輸入資料沒有預先依 key 排序，
# 相同的 key 可能會被分成多組，造成分組結果不正確。
#
# 正確用法：先排序，再用 groupby。這樣才能保證同一組的 key 連續出現。

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# 沒排序：07/02 會被分成兩段（因為 groupby 只看「連續」）
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)

# 排序後：同 date 才會連在一起，分組才正確
rows.sort(key=itemgetter('date'))
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)
