"""U09: groupby 沒排序時只會分相鄰群組。"""

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

print('未排序直接 groupby:')
for k, g in groupby(rows, key=itemgetter('date')):
    print(k, list(g))

print('\n排序後 groupby:')
rows.sort(key=itemgetter('date'))
for k, g in groupby(rows, key=itemgetter('date')):
    print(k, list(g))
