# U9. groupby 為何一定要先 sort（1.15）
# 展示 groupby 只分組「連續」相同元素的特性及為何需要排序

# 導入 groupby 和 itemgetter
from itertools import groupby
from operator import itemgetter

# 日期未排序的原始記錄
rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},  # 日期亂序
    {'date': '07/02/2012', 'x': 3},
]

# ❌ 沒排序的結果：groupby 只分組「連續」相同的元素
print("未排序的結果：")
for k, g in groupby(rows, key=itemgetter('date')):
    group_list = list(g)  # 消耗迭代器
    print(f"{k}: {group_list}")
# 輸出：
# 07/02/2012: [{'date': '07/02/2012', 'x': 1}]        <- 第 1 組
# 07/01/2012: [{'date': '07/01/2012', 'x': 2}]        <- 第 2 組（因為不連續）
# 07/02/2012: [{'date': '07/02/2012', 'x': 3}]        <- 第 3 組（重複）
# 問題：同一個日期 07/02/2012 被分成了兩組！

# ✓ 排序後的結果：相同日期變成連續，groupby 才能正確分組
rows.sort(key=itemgetter('date'))  # 先按日期排序
print("\n排序後的結果：")
for k, g in groupby(rows, key=itemgetter('date')):
    group_list = list(g)  # 消耗迭代器
    print(f"{k}: {group_list}")
# 輸出：
# 07/01/2012: [{'date': '07/01/2012', 'x': 2}]        <- 第 1 組
# 07/02/2012: [{'date': '07/02/2012', 'x': 1}, {'date': '07/02/2012', 'x': 3}]  <- 第 2 組
# 現在 07/02/2012 的兩筆記錄被正確地分在一起

# 核心概念：
# groupby 是為了節省記憶體而設計的
# 它只比較相鄰元素是否相同
# 如果要分組所有相同的值，必須先排序確保它們相鄰
