"""R6. 多值字典 defaultdict / setdefault（1.6）

這個範例示範兩種常見技巧：
1. defaultdict：當 key 不存在時，自動建立預設值。
2. setdefault：手動在一般 dict 中補上預設值。

常見用途：
- 一個 key 對應多個值（例如分組、統計、收集資料）。
"""

from collections import defaultdict

# defaultdict(list)：當某個 key 第一次出現時，自動給它一個空 list
d = defaultdict(list)
# 因為 d['a'] 會自動變成 []，所以可以直接 append
d['a'].append(1); d['a'].append(2)

# defaultdict(set)：當 key 第一次出現時，自動給它一個空 set
d = defaultdict(set)
# set 會自動去重複，適合收集不重複的值
d['a'].add(1); d['a'].add(2)

# 一般 dict 本身沒有自動建立預設值的功能
d = {}
# setdefault(key, default) 的意思是：
# - 如果 key 不存在，就先放入 default
# - 然後回傳該 key 對應的值
d.setdefault('a', []).append(1)
