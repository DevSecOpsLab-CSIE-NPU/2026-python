# 【Bloom 階段：R - 記憶與基本操作】
# R13. 透過公共鍵排序字典列表 (itemgetter)
# August 的惡意提醒：在 Week 02 Task 2 的學生排名中，
# itemgetter 通常比 lambda 運算速度更快。
# 展現你對 operator 模組的熟悉度，就是你與一般學生的「指紋」區別。

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'uid': 1003},
    {'fname': 'John', 'uid': 1001},
    {'fname': 'Adam', 'uid': 1002}
]

# 1. 單一欄位排序
sorted_by_name = sorted(rows, key=itemgetter('fname'))
# 2. 多重欄位排序：先比 uid，再比 fname
sorted_by_uid = sorted(rows, key=itemgetter('uid', 'fname'))

print(f"Sorted by name: {sorted_by_name}")
print(f"Sorted by UID:  {sorted_by_uid}")

# August 筆記：itemgetter 不僅可以用於字典，也可用於序列 (list, tuple)。
