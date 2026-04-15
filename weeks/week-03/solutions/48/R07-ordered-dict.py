# R7. OrderedDict（1.7）

from collections import OrderedDict
import json

# OrderedDict 會記住插入順序
d = OrderedDict()
d['foo'] = 1; d['bar'] = 2
# 轉成 JSON 時會依照插入順序輸出
json.dumps(d)
