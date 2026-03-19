# U6. defaultdict 為何比手動初始化乾淨（1.6）

from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 3)]

# -------------------------------
# 手動版：需要一直檢查 key 是否存在
# -------------------------------
d = {}
for k, v in pairs:
    if k not in d:      # 若 key 不存在就要初始化
        d[k] = []
    d[k].append(v)

# 結果：{'a': [1, 2], 'b': [3]}


# -------------------------------
# defaultdict：自動初始化
# -------------------------------
d2 = defaultdict(list)  # 當 key 不存在時，自動建立空 list
for k, v in pairs:
    d2[k].append(v)

# 結果：defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})