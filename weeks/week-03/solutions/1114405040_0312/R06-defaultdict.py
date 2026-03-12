# R6. 多值字典 defaultdict / setdefault（Mapping Keys to Multiple Values）—— Python Cookbook 1.6

from collections import defaultdict

# ── 方法一：defaultdict(list) ─────────────────────────────
# 當 key 不存在時，自動初始化為空 list，省去手動判斷
# 適合「一個 key 對應多個有序值」的場景（可重複）
d = defaultdict(list)
d['a'].append(1)   # d = {'a': [1]}
d['a'].append(2)   # d = {'a': [1, 2]}

# ── 方法二：defaultdict(set) ──────────────────────────────
# 預設值為空 set，自動去重
# 適合「一個 key 對應多個唯一值」的場景
d = defaultdict(set)
d['a'].add(1)   # d = {'a': {1}}
d['a'].add(2)   # d = {'a': {1, 2}}
d['a'].add(1)   # 重複加入 1，set 自動去重，仍是 {1, 2}

# ── 方法三：普通 dict + setdefault ───────────────────────
# setdefault(key, default) 的行為：
#   - 若 key 已存在：直接回傳現有值（不覆蓋）
#   - 若 key 不存在：插入 default 並回傳 default
# 比 defaultdict 多一次判斷，但不需要額外 import
d = {}
d.setdefault('a', []).append(1)   # d = {'a': [1]}
# 再次呼叫時 'a' 已存在，setdefault 回傳既有 list，再 append
