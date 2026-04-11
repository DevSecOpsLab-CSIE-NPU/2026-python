# U9. groupby 為何一定要先 sort（1.15）

from itertools import groupby
from operator import itemgetter

# 原始資料：日期是交錯的 (07/02 -> 07/01 -> 07/02)
rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# ── 1. 錯誤示範：未排序直接分組 ───────────────────────
# 原因：groupby 的運作邏輯是「線性掃描」。
# 它只會檢查「當前項」是否與「前一項」的 key 相同。
# 在這個例子中，第一個 07/02 與最後一個 07/02 之間被 07/01 隔開了，
# 因此 07/02 會被誤認為兩個獨立的群組，這通常不符合我們的預期。
for k, g in groupby(rows, key=itemgetter('date')):
    print(f"分組標籤：{k}, 成員數量：{len(list(g))}")
    # 結果會產出 3 個群組，而不是 2 個。

# ── 2. 正確做法：先根據分組鍵進行排序 ─────────────────
# 透過排序 (Sort)，我們強迫所有擁有相同日期 (date) 的資料必須「相鄰」。
# itemgetter('date') 是高效提取字典鍵值的方法，作為排序的基準 (key)。
rows.sort(key=itemgetter('date'))

# 排序後的資料：(07/01 -> 07/02 -> 07/02)
# 此時相同的日期連在一起，groupby 就能正確地將它們歸入同一個群組。
for k, g in groupby(rows, key=itemgetter('date')):
    # 這裡的 g 是一個迭代器，包含該日期下的所有原始字典
    items = list(g)
    print(f"正確分組：{k}, 成員：{items}")
    # 結果會產出 2 個群組：07/01 一組，07/02 一組（內含兩筆資料）。