# R15. 分組 groupby（1.15）
#
# 觀念重點：
# 1) groupby 只會把「相鄰且 key 相同」的資料分成同一組。
# 2) 所以分組前通常要先 sort，讓相同 key 的資料排在一起。
# 3) groupby 回傳的群組是 iterator，用過就會被消耗。

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/01/2012', 'address': '...'},
    {'date': '07/02/2012', 'address': '...'},
]

# 先按 date 排序，確保同日期資料連續出現。
rows.sort(key=itemgetter('date'))

# date 是目前分組鍵；items 是該組資料的 iterator。
for date, items in groupby(rows, key=itemgetter('date')):
    for i in items:
        # 實務上可在這裡做輸出、彙整、寫檔等操作。
        pass
