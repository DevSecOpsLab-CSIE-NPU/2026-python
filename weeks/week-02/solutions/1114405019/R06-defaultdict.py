# R6. 多值字典 defaultdict / setdefault（1.6）

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1); d['a'].append(2)

d = defaultdict(set)
d['a'].add(1); d['a'].add(2)

d = {}
d.setdefault('a', []).append(1)
