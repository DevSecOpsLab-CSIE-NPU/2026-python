# 【Bloom 階段：U - 理解與進階應用】
# U9. groupby 之前的關鍵排序 (Sort Before Groupby)
# August 的惡意提醒：這是本週最致命的地雷。
# 如果不排序就用 groupby，資料會被拆得支離破碎。

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3}, # 這裡與第一項日期相同但「不連續」
]

# ❌ 錯誤示範：未排序直接分組
print("Result WITHOUT sorting:")
for k, g in groupby(rows, key=itemgetter('date')):
    print(f"Date {k}: {list(g)}") # 你會看到 07/02 被分成了兩組！

# ✅ 正確示範：先 sort，確保相同日期相連
print("\nResult WITH sorting:")
rows.sort(key=itemgetter('date'))
for k, g in groupby(rows, key=itemgetter('date')):
    print(f"Date {k}: {list(g)}") # 這樣才是正確的分組
