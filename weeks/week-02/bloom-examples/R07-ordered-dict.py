"""R07: OrderedDict 保留插入順序。"""

from collections import OrderedDict
import json

od = OrderedDict()
od['foo'] = 1
od['bar'] = 2
od['spam'] = 3

print('OrderedDict 順序:', list(od.keys()))
print('轉成 JSON:', json.dumps(od, ensure_ascii=False))
