# U07 OrderedDict 的取捨
# 重點：可明確維持插入順序；在較舊 Python 版本中特別有用。

from collections import OrderedDict

d = OrderedDict()
d["foo"] = 1
d["bar"] = 2

# OrderedDict 會保留插入順序（foo 在 bar 前）。
# 注意：現代 Python 的一般 dict 也已保序，但 OrderedDict
# 仍有部分專用方法與語意場景（例如 move_to_end）。
