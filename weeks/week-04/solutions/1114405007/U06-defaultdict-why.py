# U6. defaultdict 為何比手動初始化乾淨（1.6）

from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 3)]

# 手動版：一直判斷 key 是否存在
d = {}
for k, v in pairs:
    if k not in d:
        # 第一次看到這個 key 時，先建立空串列
        d[k] = []
    d[k].append(v)

# defaultdict：當 key 不存在時，自動建立 list，省掉初始化分支
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)

print('手動版:', d)
print('defaultdict 版:', dict(d2))
