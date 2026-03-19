# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

# OrderedDict 會記住插入順序：
# → [('foo', 1), ('bar', 2)]