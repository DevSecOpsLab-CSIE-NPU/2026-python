# U6. defaultdict 為何比手動初始化乾淨（1.6）
#
# 觀念重點：
# - defaultdict 在 key 首次出現時，會自動用預設工廠建立初值。
# - 這裡用 list 當工廠，代表新 key 會自動得到 []。

from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 3)]

# 手動版：每次都要先判斷 key 是否存在，再決定要不要初始化。
d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []
    d[k].append(v)

# defaultdict 版：直接 append，邏輯更精簡。
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)
