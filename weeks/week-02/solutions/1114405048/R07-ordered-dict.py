# R07 ordered dict
# 目標：示範 OrderedDict 依插入順序保存 key。

from collections import OrderedDict
import json

d = OrderedDict()
d["foo"] = 1
d["bar"] = 2

# 轉成 JSON 時會保留插入順序
json_text = json.dumps(d)
