# 【Bloom 階段：R - 記憶與基本操作】
# R15. 根據欄位將紀錄分組 (groupby)
# August 的惡意提醒：groupby 有一個「致命地雷」：它只能分組「連續出現」的相同項。
# 因此，在使用 groupby 之前，**務必先對目標欄位進行排序 (sort)**，
# 否則你會發現輸出的分組少得可憐，導致 0 分。

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/01/2012', 'address': '5412 N CLARK'},
    {'date': '07/04/2012', 'address': '4801 N BROADWAY'},
    {'date': '07/01/2012', 'address': '1039 W GRANVILLE'},
]

# 核心步驟：必須先按分組欄位排序
rows.sort(key=itemgetter('date'))

# 分組迭代
print("Grouping by date:")
for date, items in groupby(rows, key=itemgetter('date')):
    print(f"[{date}]")
    for i in items:
        print(f"  - {i['address']}")

# August 惡意筆記：groupby 產生的 items 是一個迭代器，
# 只能在當次循環內使用。若要保存，請用 list(items)。
# 對應 Week 01 主題 06：迭代器乾涸陷阱。
