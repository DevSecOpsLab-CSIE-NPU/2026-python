# R6. 多值字典 defaultdict / setdefault（1.6）

from collections import defaultdict

# defaultdict(list)：第一次存取不存在 key 時自動建立空串列
d = defaultdict(list)
d['a'].append(1); d['a'].append(2)

# defaultdict(set)：同理自動建立空集合
d = defaultdict(set)
d['a'].add(1); d['a'].add(2)

# 一般 dict 可用 setdefault 達到類似效果
d = {}
d.setdefault('a', []).append(1)
