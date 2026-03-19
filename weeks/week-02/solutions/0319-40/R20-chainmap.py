# R20. ChainMap 合併映射（1.20）

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)

# 直接印出查詢結果
print("c['x'] =", c['x'])
print("c['y'] =", c['y'])
print("c['z'] =", c['z'])  # 會先取到 a 的 z
print("ChainMap 內容 =", dict(c))
