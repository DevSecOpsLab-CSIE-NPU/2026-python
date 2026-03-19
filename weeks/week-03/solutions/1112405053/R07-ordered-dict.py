# R7. OrderedDict（1.7）

from collections import OrderedDict
import json

# OrderedDict 會保留插入順序（新版 dict 也保序，但此處為示範）
d = OrderedDict()
d['foo'] = 1; d['bar'] = 2

# 轉成 JSON 時會依插入順序輸出
json.dumps(d)
