# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）
"""
本範例說明 collections.OrderedDict 的用途與代價。

OrderedDict 可保留元素的插入順序（insertion order），
這對於需要按照加入順序遍歷或輸出資料的場合非常有用。

但是，為了維持這個順序，它會額外維護一個鏈結結構（linked list）
來記錄元素順序，這會導致較一般 dict 有更高的記憶體開銷。

Python 3.7 之後普通 dict 已經保留插入順序，因此 OrderedDict 的
主要優勢變成了提供一些特殊方法（例如 move_to_end、popitem(last=True)）。
"""

from collections import OrderedDict

# 建立 OrderedDict 並依序插入鍵值
# OrderedDict 會記住插入順序，因此後續遍歷會保持相同順序
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

# 對比一般 dict：
# - Python 3.7+ 的 dict 也會保留插入順序，但內部實作並不會保留額外鏈結結構。
# - OrderedDict 則會額外維持「前後節點連結」，因此相對更吃記憶體。

# OrderedDict 特色方法（Dict 無法直接使用）:
# - move_to_end(key, last=True)：將指定鍵移到最前或最後
# - popitem(last=True)：彈出最前或最後的鍵值對

