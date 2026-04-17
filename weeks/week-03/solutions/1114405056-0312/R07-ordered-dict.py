# R7. OrderedDict（1.7）
# =========================================================
# OrderedDict 是有序字典，能夠記住元素插入的順序
# 遍歷時會按照鍵的插入順序返回元素
# 在 Python 3.7+ 中，普通字典已自動保持插入順序
# 但 OrderedDict 仍有一些特殊場景有用，如：
# 1. 需要比較相等性時忽略順序差異
# 2. 需要方便的 popitem(last=True/False) 控制彈出順序
# =========================================================

from collections import OrderedDict
import json

# 創建有序字典並添加鍵值對
d = OrderedDict()

# 鍵的順序會被記住：d = {'foo': 1, 'bar': 2}
d['foo'] = 1
d['bar'] = 2

# JSON 序列化時順序會被保留
# 結果：'{"foo": 1, "bar": 2}'
json.dumps(d)

# =========================================================
# OrderedDict 的其他常用方法：
# =========================================================

# popitem(last=True): 彈出最後一個（或第一個）鍵值對
# last=True（預設）：從右端（最後）彈出，即 LIFO
# last=False：從左端（最先）彈出，即 FIFO

# move_to_end(key, last=True): 將指定鍵移動到字典的末端或前端
# d.move_to_end('foo') 將 'foo' 移到最後
# d.move_to_end('foo', last=False) 將 'foo' 移到最前
