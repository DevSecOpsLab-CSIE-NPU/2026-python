# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）
#
# 觀念重點：
# - OrderedDict 會明確維護插入順序。
# - 維護順序通常需要額外資料結構，因此記憶體成本較高。
# - 在新版本 Python 中，普通 dict 也保留插入順序；但 OrderedDict
#   仍有一些語意/API（例如順序相關操作）可用於特定情境。

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

# 若重點只是一般查表，普通 dict 常已足夠；
# 若你需要強調「順序語意」或特定 OrderedDict API，再使用它。
