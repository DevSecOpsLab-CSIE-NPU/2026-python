# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

# 顯示插入順序
print('OrderedDict 內容 =', d)
print('keys 順序 =', list(d.keys()))

# 補充：一般 dict（Python 3.7+）也保序，但 OrderedDict 仍有特定操作價值
normal_dict = {'foo': 1, 'bar': 2}
print('一般 dict 內容 =', normal_dict)
print('一般 dict keys 順序 =', list(normal_dict.keys()))
