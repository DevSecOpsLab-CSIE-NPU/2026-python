# R6. 多值字典 defaultdict / setdefault（1.6）

from collections import defaultdict

# defaultdict(list): key 不存在時自動建立空 list
d = defaultdict(list)
d['a'].append(1); d['a'].append(2)

# defaultdict(set): key 不存在時自動建立空 set
d = defaultdict(set)
d['a'].add(1); d['a'].add(2)

# 一般 dict 也可用 setdefault 達到類似效果
d = {}
d.setdefault('a', []).append(1)
