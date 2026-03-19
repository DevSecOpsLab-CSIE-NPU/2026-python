"""R15. 分組 groupby（1.15）

範例說明：示範如何使用 itertools.groupby 根據 dict 中的某個鍵（此處為 'date'）進行分組。
注意：使用 groupby 前必須先對資料依相同的鍵排序，才能正確分組。
"""

from itertools import groupby  # 用於產生分組的 iterator
from operator import itemgetter  # 提供根據 dict 鍵取值的快捷函數

# 範例資料：每個元素為一個 dict，包含 'date' 與 'address' 欄位 
rows = [
    {'date': '07/01/2012', 'address': '...'},
    {'date': '07/02/2012', 'address': '...'}
]

# 先依照 date 欄位排序，因為 groupby 只會將相鄰（已排序）項目視為同一組
rows.sort(key=itemgetter('date'))

# 使用 groupby 進行分組，key=itemgetter('date') 表示以 'date' 欄位為分組依據
for date, items in groupby(rows, key=itemgetter('date')):
    # date: 當前分組的鍵（例如 '07/01/2012'）
    # items: 屬於該分組的項目 iterator（可逐一迭代）
    for i in items:
        # 在此處處理每個分組內的項目；範例中不作實際處理，保留 pass
        pass

# R15. 分組 groupby（1.15）

from itertools import groupby
from operator import itemgetter

rows = [{'date': '07/01/2012', 'address': '...'}, {'date': '07/02/2012', 'address': '...'}]
rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    for i in items:
        pass
