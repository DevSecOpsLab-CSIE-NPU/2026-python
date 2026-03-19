# U7. OrderedDict 的取捨：記憶體消耗（範例 1.7）
# 原理：為了維持插入順序，OrderedDict 內部使用雙向鏈結串列，這會比一般 dict 消耗多出約兩倍記憶體。

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
# 遍歷時會嚴格遵守插入順序：foo 永遠在 bar 之前