# R7. OrderedDict（1.7）

from collections import OrderedDict
import json

# OrderedDict 會保留插入順序
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3

json_text = json.dumps(d, ensure_ascii=False)
print('OrderedDict 項目順序:', list(d.items()))
print('轉成 JSON:', json_text)
