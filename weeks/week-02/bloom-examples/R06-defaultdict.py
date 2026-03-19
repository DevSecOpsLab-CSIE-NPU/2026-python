"""R06: defaultdict 與 setdefault 比較。"""

from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 3)]

# defaultdict(list): 不必先判斷 key 是否存在
d1 = defaultdict(list)
for k, v in pairs:
    d1[k].append(v)
print('defaultdict(list):', dict(d1))

# defaultdict(set): 自動建立 set，可自然去重
d2 = defaultdict(set)
for k, v in pairs + [('a', 1)]:
    d2[k].add(v)
print('defaultdict(set):', {k: sorted(v) for k, v in d2.items()})

# 一般 dict 需手動 setdefault
d3 = {}
for k, v in pairs:
    d3.setdefault(k, []).append(v)
print('dict + setdefault:', d3)
