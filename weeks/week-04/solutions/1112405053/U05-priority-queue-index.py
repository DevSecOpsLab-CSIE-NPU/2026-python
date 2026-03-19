"""U5. 優先佇列為何要加 index（1.5）

說明在使用 heapq 時，若放入的 tuple 第一個欄位相同，heapq 會嘗試比較下一個元素。
若該元素不可比較，則會拋出 TypeError；解法是加入不會重複且可比較的 index。
"""

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
