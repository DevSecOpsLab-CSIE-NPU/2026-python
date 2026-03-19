# U5. 優先佇列為何要加 index（1.5）
#
# heapq 會比較 tuple 的各個欄位來決定順序；
# 當第一個欄位（priority）相同時，會繼續比較第二個欄位。
#
# 如果你放入 (priority, item)，而 item 是自訂類別（如 Item），
# Python 會試圖比較 Item 物件（呼叫 __lt__），但它沒有實作，
# 於是會拋出 TypeError："<' not supported between instances of 'Item' and 'Item'"。
#
# 解法：在 tuple 裡加一個不會比較失敗的值（例如遞增的 index），
# 讓 heapq 可以在 priority 相同時，順序地比較這個 index。

import heapq

class Item:
    def __init__(self, name):
        self.name = name

pq = []

# 若只放 (priority, item)，同 priority 會比較 item，Item 不支援 < 會炸
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError

# 正解：加 index 避免比較 item
idx = 0
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1
