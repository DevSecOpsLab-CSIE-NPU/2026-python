"""
R07: OrderedDict

OrderedDict 會保留鍵的插入順序，序列化時可維持同樣順序。
"""

from collections import OrderedDict
import json

# 依序插入 foo、bar。
d = OrderedDict()
d["foo"] = 1
d["bar"] = 2

# 轉成 JSON 時，鍵順序會照插入順序輸出。
json.dumps(d)
