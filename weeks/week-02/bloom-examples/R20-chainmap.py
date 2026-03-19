"""R20: ChainMap 合併多個字典視圖。"""

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)

# 查找時會依序由前往後找
print('x =', c['x'])
print('y =', c['y'])
print('z =', c['z'])  # 取到 a 的 z

# 寫入只會寫到第一層字典 a
c['w'] = 100
print('a 更新後:', a)
print('b 保持不變:', b)
