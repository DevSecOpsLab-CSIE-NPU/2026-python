# R6. 多值字典 defaultdict / setdefault（1.6）

from collections import defaultdict

# defaultdict(list)：鍵不存在時自動建立空 list
list_dict = defaultdict(list)
list_dict['a'].append(1)
list_dict['a'].append(2)
print('defaultdict(list):', dict(list_dict))

# defaultdict(set)：適合去重
set_dict = defaultdict(set)
set_dict['a'].add(1)
set_dict['a'].add(2)
set_dict['a'].add(1)
print('defaultdict(set):', dict(set_dict))

# 一般 dict 可用 setdefault 達到近似效果
normal_dict = {}
normal_dict.setdefault('a', []).append(1)
print('setdefault 寫法:', normal_dict)
