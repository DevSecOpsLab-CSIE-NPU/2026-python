# R6. 多值字典 defaultdict / setdefault（1.6）

from collections import defaultdict

# ── 1. 使用 defaultdict 配合 list ────────────────────
# 當存取的鍵不存在時，自動呼叫 list() 建立一個空列表作為預設值
d = defaultdict(list)
# 不需判斷 'a' 是否存在，直接 append 即可
d['a'].append(1); d['a'].append(2)
# 結果：{'a': [1, 2]}

# ── 2. 使用 defaultdict 配合 set ─────────────────────
# 當希望同一個鍵下的值不重複時（自動去重），可以使用 set
d = defaultdict(set)
# set 使用 add() 方法而非 append()
d['a'].add(1); d['a'].add(2)
# 結果：{'a': {1, 2}}

# ── 3. 使用原生字典的 setdefault 方法 ────────────────
# 這是標準字典 (dict) 內建的方法，不需額外匯入模組
d = {}

# setdefault(key, default_value) 的邏輯：
# 1. 如果 'a' 不在字典中，則執行 d['a'] = [] 並回傳該列表。
# 2. 如果 'a' 已存在，則直接回傳已存在的物件。
# 接著直接對回傳的物件執行 .append(1)
d.setdefault('a', []).append(1)
# 結果：{'a': [1]}