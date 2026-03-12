# R7. OrderedDict（1.7）
# 保留插入順序的字典，可在序列化時顯示順序。

from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1; d['bar'] = 2
print("ordered dict ->", d)
print("json dumps preserves order ->", json.dumps(d))
