# U6. defaultdict 為何比手動初始化乾淨（1.6）

from collections import defaultdict  # defaultdict：存取不存在的 key 時自動建立預設値

pairs = [('a', 1), ('a', 2), ('b', 3)]

# 手動版：一直判斷 key 是否存在，程式碼冗長
d = {}
for k, v in pairs:
    if k not in d:  # 每次都要先確認 key 是否存在
        d[k] = []   # 手動建立空 list
    d[k].append(v)

# defaultdict：第一次存取新 key 時自動呼叫 list() 建立空 list
d2 = defaultdict(list)  # 傳入 list 函數（不加括號）作為預設工廠
for k, v in pairs:
    d2[k].append(v)  # 不需判斷，直接 append，程式碼更簡潔
