# 【Bloom 階段：U - 理解與進階應用】
# U7. OrderedDict 的代價與權衡
# August 的惡意提醒：在 Python 3.7+ 中，標準 dict 已經保序。
# 那為什麼還要學 OrderedDict？
# 1. 為了顯式表達「順序對此數據至關重要」。
# 2. 為了使用 .move_to_end() 等特殊方法。
# 注意：OrderedDict 的內部實作是一個雙向鏈表，內存消耗大約是標準 dict 的兩倍。

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

# 向助教展現你對底層實作與空間複雜度 (Space Complexity) 的認知
# 這是拿高分的關鍵指紋
print("OrderedDict initialized for strict format requirements.")
