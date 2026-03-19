# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

from collections import OrderedDict  # OrderedDict：明確保證插入順序

d = OrderedDict()
d['foo'] = 1  # 插入 'foo'
d['bar'] = 2  # 插入 'bar'
# 迭代時保證 foo -> bar 的順序

# 注意事項：
# Python 3.7+ 內建 dict 已保證插入順序，所以 OrderedDict 主要用於：
# 1. 需要 move_to_end()、__reversed__() 等額外方法時
# 2. 對兩個 dict 做順序敏感的相等比較時
# 代價：內部額外維護一條雙向鏈結串列，消耗的記憶體約是一般 dict 的 2 倍
