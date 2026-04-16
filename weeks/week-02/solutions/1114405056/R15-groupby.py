# R15. 分組 groupby（1.15）

from itertools import groupby
from operator import itemgetter

rows = [{'date': '07/01/2012', 'address': '...'}, {'date': '07/02/2012', 'address': '...'}]
rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    for i in items:
        pass
