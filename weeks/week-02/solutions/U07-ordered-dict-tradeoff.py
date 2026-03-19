# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）
#
# 在 Python 3.7+ 的 dict 已經保留插入順序，OrderedDict 與 dict 行為相似，
# 但它有一些額外功能（例如 move_to_end）且內部用了一個雙向連結串列來
# 維持順序。
#
# 這代表 OrderedDict 會比普通 dict 佔用更多記憶體（用來儲存指標/節點），
# 但若有需要控制「插入順序」或進行「順序操作」，它仍是有用的。

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
# 你能解釋：為了維持插入順序，它需要額外結構（因此更耗記憶體）
