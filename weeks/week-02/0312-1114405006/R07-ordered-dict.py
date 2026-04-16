# R7. OrderedDict（1.7）
#
# OrderedDict 會記住插入順序：
# 1. 早期 Python 版本中，這是特別有用的資料結構。
# 2. 當需要序列化成 JSON 時，順序可被保留。
# 3. 現代 Python 的一般 dict 也會保留插入順序，但這個範例是為了說明 OrderedDict 的用途。

from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1; d['bar'] = 2
json.dumps(d)
