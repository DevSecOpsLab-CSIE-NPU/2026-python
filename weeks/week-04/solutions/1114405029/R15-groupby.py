# R15. 分組 groupby（1.15）

from itertools import groupby
from operator import itemgetter

# 原始資料：包含日期與地址的字典列表
rows = [
    {'date': '07/01/2012', 'address': '5412 N CLARK ST'},
    {'date': '07/04/2012', 'address': '1060 W ADDISON ST'},
    {'date': '07/02/2012', 'address': '1039 W GRANVILLE AVE'},
    {'date': '07/01/2012', 'address': '4801 N BROADWAY'},
    {'date': '07/02/2012', 'address': '5800 E 58TH ST'},
]

# 重要步驟：使用 groupby 之前，必須先根據「分組欄位」進行排序
# 因為 groupby 只會掃描「連續」的重複項。如果不排序，相同日期的資料若不相鄰，將無法被歸在同一組。
# itemgetter('date') 的效能比 lambda x: x['date'] 更快
rows.sort(key=itemgetter('date'))

# groupby(資料來源, key=分組基準)
# 它會回傳一個迭代器，每次產生 (群組標籤, 該組內容的迭代器)
for date, items in groupby(rows, key=itemgetter('date')):
    print(f"日期：{date}")
    
    # items 是一個迭代器，包含所有屬於該日期（date）的原始字典資料
    for i in items:
        # 在這裡處理每一筆分組後的資料
        print(f"  - {i}")
        pass