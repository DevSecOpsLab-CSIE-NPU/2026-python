# R20. ChainMap 合併映射（1.20）

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)

c['x']
c['z']  # 取到 a 的 z
