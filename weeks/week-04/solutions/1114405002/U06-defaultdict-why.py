# U06 為什麼用 defaultdict
# 重點：可省去「key 不存在就先初始化」的樣板程式。

from collections import defaultdict

pairs = [("a", 1), ("a", 2), ("b", 3)]

# 傳統 dict 寫法：每次 append 前都要檢查 key 是否已存在。
d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []
    d[k].append(v)

# defaultdict(list) 會在缺 key 時自動建立空 list。
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)
