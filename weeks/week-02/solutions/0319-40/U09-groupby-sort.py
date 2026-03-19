# U9. groupby 為何一定要先 sort（1.15）

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

print('=== 沒排序前 ===')
for key, group in groupby(rows, key=itemgetter('date')):
    items = list(group)
    print(key, '->', items)

print('\n=== 排序後 ===')
rows.sort(key=itemgetter('date'))
for key, group in groupby(rows, key=itemgetter('date')):
    items = list(group)
    print(key, '->', items)
