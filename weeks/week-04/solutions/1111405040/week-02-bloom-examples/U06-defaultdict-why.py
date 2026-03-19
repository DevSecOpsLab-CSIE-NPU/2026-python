"""
U06: defaultdict 的用途

當 key 第一次出現時，可以自動建立預設容器。
"""

from collections import defaultdict


pairs = [("a", 1), ("a", 2), ("b", 3)]

# 一般 dict 需要先判斷 key 是否存在。
d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []
    d[k].append(v)

# defaultdict 可以把這段初始化動作省略掉。
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)
