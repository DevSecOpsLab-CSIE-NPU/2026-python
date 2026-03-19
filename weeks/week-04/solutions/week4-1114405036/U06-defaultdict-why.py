# U6. defaultdict 為何更好用（範例 1.6）
# 原理：自動初始化不存在的 key，省去 if k not in d 的判斷分支。

from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 3)]

# 使用 defaultdict(list)，當 key 不存在時自動建立一個空的 []
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)