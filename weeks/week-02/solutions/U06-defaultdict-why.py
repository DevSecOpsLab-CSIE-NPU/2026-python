# U6. defaultdict 為何比手動初始化乾淨（1.6）
#
# 在字典中為每個 key 存放 list/集合/計數等資料時，常常需要先確保該 key 存在，
# 否則要先建立空容器再 append/extend。
#
# defaultdict 可以自動在 key 不存在時建立預設值（透過 factory function），
# 讓程式碼更簡潔，也更易於閱讀。

from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 3)]

# 手動版：一直判斷 key 是否存在
# 如果 key 不存在，就先建立一個空 list
d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []
    d[k].append(v)

# defaultdict：省掉初始化分支，未曾出現的 key 會自動初始化為 list()
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)
