# R20. ChainMap 合併映射（1.20）
#
# 觀念重點：
# - ChainMap 可把多個 dict 串成「單一查詢視圖」，不需真的合併資料。
# - 查找時會由左到右搜尋，先找到就回傳。

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# c 會先看 a，再看 b。
c = ChainMap(a, b)

# x 只在 a，直接取到 1。
c['x']

# z 在 a、b 都有，但因為 a 在前面，所以取到 a['z'] == 3。
c['z']
print(c)  # ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})