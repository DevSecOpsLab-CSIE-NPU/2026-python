"""U07: OrderedDict 的優缺點說明。"""

from collections import OrderedDict

od = OrderedDict()
od['foo'] = 1
od['bar'] = 2
od['spam'] = 3

print('維持插入順序:', list(od.items()))

# 說明：
# 1. 需要穩定順序輸出時很好用。
# 2. Python 3.7+ 一般 dict 也保序，但 OrderedDict 仍提供 move_to_end 等操作。
od.move_to_end('foo')
print('move_to_end 後:', list(od.items()))
