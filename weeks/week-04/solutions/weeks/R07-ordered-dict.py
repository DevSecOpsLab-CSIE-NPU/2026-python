# R7. OrderedDict（1.7）

from collections import OrderedDict
import json

# 建立一個 OrderedDict（有順序的字典）
# 與一般 dict 不同的是，它會「記住插入順序」
d = OrderedDict()

# 依序加入鍵值
d['foo'] = 1
d['bar'] = 2

# json.dumps() 會依照插入順序輸出
# 結果會是 {"foo": 1, "bar": 2}
json.dumps(d)