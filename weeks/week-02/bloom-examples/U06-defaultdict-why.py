# U6. defaultdict 為何比手動初始化乾淨（1.6）

from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 3)]

# 手動版：一直判斷 key 是否存在
d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []
    d[k].append(v)

# defaultdict：省掉初始化分支
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)
