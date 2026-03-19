# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
# 你能解釋：為了維持插入順序，它需要額外結構（因此更耗記憶體）
