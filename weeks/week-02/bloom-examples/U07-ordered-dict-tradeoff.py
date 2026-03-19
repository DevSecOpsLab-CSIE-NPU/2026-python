"""
U07: OrderedDict 的取捨

它會保留插入順序，但也會多一點維護成本。
"""

from collections import OrderedDict


d = OrderedDict()
d["foo"] = 1
d["bar"] = 2

# 當你需要明確控制鍵的輸出順序時，OrderedDict 會比較好用。
