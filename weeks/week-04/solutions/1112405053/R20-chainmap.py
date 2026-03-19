"""R20. ChainMap 合併映射（1.20）

示範 collections.ChainMap 如何將多個映射（dict）組合在一起，並
說明鍵查找時的遮蔽（shadowing）行為。
"""

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)

# 從 ChainMap 讀取鍵：會依照傳入的映射順序查找，遇到第一個匹配的鍵即回傳
c['x']
# c['z'] 會回傳來自 a 的值（3），因為 a 在 b 之前，a 的 z 遮蔽了 b 的 z
c['z']  # 取到 a 的 z 
