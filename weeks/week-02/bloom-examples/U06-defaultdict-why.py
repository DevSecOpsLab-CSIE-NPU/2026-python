"""U06: defaultdict 為何能省去「先初始化 key」的樣板碼。"""

from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 3)]

# 一般 dict 版本
normal = {}
for k, v in pairs:
    if k not in normal:
        normal[k] = []
    normal[k].append(v)
print('一般 dict:', normal)

# defaultdict 版本
dd = defaultdict(list)
for k, v in pairs:
    dd[k].append(v)
print('defaultdict:', dict(dd))
