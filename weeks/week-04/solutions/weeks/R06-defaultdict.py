# R6. 多值字典 defaultdict / setdefault（1.6）

from collections import defaultdict

# 使用 defaultdict(list)
# 當 key 不存在時，自動建立一個空的 list 作為預設值
d = defaultdict(list)
d['a'].append(1)   # d = {'a': [1]}
d['a'].append(2)   # d = {'a': [1, 2]}

# 使用 defaultdict(set)
# 當 key 不存在時，自動建立一個空的 set 作為預設值
d = defaultdict(set)
d['a'].add(1)      # d = {'a': {1}}
d['a'].add(2)      # d = {'a': {1, 2}}

# 使用一般 dict + setdefault()
d = {}
# setdefault('a', [])：若 'a' 不存在，建立 'a': []
# 然後回傳該列表，再 append(1)
d.setdefault('a', []).append(1)   # d = {'a': [1]}