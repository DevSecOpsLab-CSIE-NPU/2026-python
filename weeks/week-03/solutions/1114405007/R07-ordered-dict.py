# R7: OrderedDict（保留插入順序的字典）
# 觀念：在舊版 Python 常用來確保鍵值順序穩定。
# 補充：Python 3.7+ 的內建 dict 也保有插入順序，但 OrderedDict 仍有其 API 用途。

from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
# 後插入的鍵會排在後面
d['bar'] = 2

# 轉成 JSON 時會依照插入順序輸出
json.dumps(d)
