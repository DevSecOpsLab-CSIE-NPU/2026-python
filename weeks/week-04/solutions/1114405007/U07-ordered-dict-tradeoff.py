# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

from collections import OrderedDict

# OrderedDict 會明確維護插入順序
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

# 你能解釋：為了維持插入順序，它需要額外結構（因此更耗記憶體）
print('OrderedDict 內容:', list(d.items()))
