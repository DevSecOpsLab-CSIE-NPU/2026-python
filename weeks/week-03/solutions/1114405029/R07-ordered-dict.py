# R7. OrderedDict（1.7）
#
# OrderedDict 是「有序字典」：
# - 會記錄 key 的插入順序。
# - 走訪（iterate）或序列化時，可保留這個順序。
#
# 補充：Python 3.7+ 的一般 dict 也保證插入順序，
# 所以很多情況下不一定要用 OrderedDict。
# 但 OrderedDict 仍有一些專屬操作（例如 move_to_end）在特定場景很實用。

from collections import OrderedDict
import json


# 建立一個 OrderedDict
d = OrderedDict()

# 依序插入兩個鍵值
# 插入順序為：foo -> bar
d['foo'] = 1; d['bar'] = 2

# 轉成 JSON 字串
# 在這裡會依照目前字典順序輸出，結果類似：
# '{"foo": 1, "bar": 2}'
# 注意：這行沒有指定變數接結果，因此字串不會被保留。
json.dumps(d)


# 讀懂這份程式的步驟：
# 1. 先看 key 插入順序（誰先寫進字典）。
# 2. 再看後續操作是否依賴順序（例如輸出、比對、顯示）。
# 3. json.dumps 會把目前映射內容轉字串，通常會反映字典的迭代順序。
# 4. 若只需要「保序」且使用 Python 3.7+，一般 dict 多半已足夠。
