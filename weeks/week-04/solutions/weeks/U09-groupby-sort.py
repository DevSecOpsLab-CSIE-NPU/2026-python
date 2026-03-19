# U9. groupby 為何一定要先 sort（1.15）

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# -------------------------------
# ❌ 沒排序：07/02 會被分成兩段
# 因為 groupby 只會把「連續」的相同 key 視為同一組
# -------------------------------
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)   # '07/02' 會出現兩次，因為資料不連續


# -------------------------------
# ✔ 排序後：相同 date 才會連在一起
# 分組才會正確
# -------------------------------
rows.sort(key=itemgetter('date'))

for k, g in groupby(rows, key=itemgetter('date')):
    list(g)   # '07/02' 只會有一組