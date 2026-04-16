# R6. 多值字典 defaultdict / setdefault（1.6）
#
# defaultdict 的好處是：
# 1. 存取不存在的 key 時，會自動建立預設容器。
# 2. 用 list 可以累積多個值，用 set 可以自動去重。
# 3. setdefault 是另一種寫法，但通常可讀性與便利性不如 defaultdict。

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1); d['a'].append(2)

d = defaultdict(set)
d['a'].add(1); d['a'].add(2)

d = {}
d.setdefault('a', []).append(1)
