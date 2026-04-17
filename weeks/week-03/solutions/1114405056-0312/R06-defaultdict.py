# R6. 多值字典 defaultdict / setdefault（1.6）
# =========================================================
# 當需要一個鍵對應多個值時，可以使用 defaultdict
# defaultdict 會自動為不存在的鍵創建默認值，避免 KeyError
# 與普通字典的 setdefault() 方法有類似的效果
# =========================================================

from collections import defaultdict

# defaultdict(list): 當鍵不存在時，自動創建空列表作為默认值
d = defaultdict(list)

# 鍵 'a' 不存在時會自動創建空列表 []
# 等價於：if 'a' not in d: d['a'] = []
d['a'].append(1)  # d = {'a': [1]}
d['a'].append(2)  # d = {'a': [1, 2]}

# defaultdict(set): 當鍵不存在時，自動創建空集合作為默认值
d = defaultdict(set)

# 集合的 append 改為 add（集合無序不重複）
d['a'].add(1)  # d = {'a': {1}}
d['a'].add(2)  # d = {'a': {1, 2}}

# =========================================================
# 傳統方式：使用普通字典 + setdefault
# =========================================================

d = {}

# setdefault(key, default):
# 如果鍵存在，返回該鍵的值；如果不存在，設定為 default 並返回
# 等價於 defaultdict 的行為，但語法更繁瑣
d.setdefault('a', []).append(1)
# 內部過程：d['a'] 不存在，所以 d['a'] = []，然後 [].append(1)
