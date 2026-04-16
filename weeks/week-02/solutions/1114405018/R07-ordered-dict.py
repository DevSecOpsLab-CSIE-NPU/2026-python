"""R7. OrderedDict（1.7）

OrderedDict 是一種「記得插入順序」的字典。
在 Python 3.7+ 一般 dict 也會保留插入順序，
但 OrderedDict 仍常見於需要明確表達「順序重要」的程式碼中。
"""

from collections import OrderedDict
import json

# 建立一個會保留插入順序的字典
d = OrderedDict()
# 先加入 foo，再加入 bar，輸出時會依照這個順序保存
d['foo'] = 1; d['bar'] = 2
# json.dumps() 會把字典轉成 JSON 字串，且會依字典的順序輸出鍵值
json.dumps(d)
