# R20. ChainMap 合併映射（1.20）
# 說明：將多個字典邏輯上合併成一個，不會建立新字典，而是按順序搜尋。

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# 合併 a 與 b
c = ChainMap(a, b)

print(c['x']) # 從 a 找到，結果為 1
print(c['y']) # a 沒找到，去 b 找，結果為 2
print(c['z']) # a 有 z，b 也有 z，但會優先取第一個出現的，結果為 3