# U9. groupby 為何一定要先 sort（1.15）

from itertools import groupby    # groupby：對連續相同 key 的元素分組
from operator import itemgetter  # itemgetter：取 dict 中指定欄位，比 lambda 效率稍高

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# 沒排序：07/02 會被分成兩段（因為 groupby 只看「連續」相同的 key）
# 這就像流水線處理：只指出「相鄰相同」的連續區段
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)  # 會產生 3 組：07/02、07/01、07/02（不正確）

# 排序後：同 date 才會連在一起，分組才正確
rows.sort(key=itemgetter('date'))  # 先依 date 排序，確保相同日期相鄰
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)  # 正確產生 2 組：07/01、07/02
