# R7. OrderedDict（1.7）

from collections import OrderedDict
import json

# ── 建立具名順序字典 ──────────────────────────────────
# OrderedDict 會記錄元素被「插入」的順序
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

# 即使是在 Python 3.7+ 標準字典已保序的背景下，
# 使用 OrderedDict 能更明確地表達這段程式碼「依賴順序」的意圖。
# 此外，兩個 OrderedDict 比較時，順序不同會被視為不相等 (d1 == d2 為 False)。

# ── 序列化為 JSON ─────────────────────────────────────
# json.dumps() 會將 Python 物件轉換為 JSON 字串。
# 由於 d 是 OrderedDict，輸出的字串會嚴格遵守 'foo' 在前、'bar' 在後的順序。
# 結果：'{"foo": 1, "bar": 2}'
json.dumps(d)