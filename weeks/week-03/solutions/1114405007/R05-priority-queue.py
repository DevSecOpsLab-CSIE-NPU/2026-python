# R5: 自製 PriorityQueue（優先佇列）
# 觀念：使用 heapq 儲存 (優先級, 次序, 物件) 來實作可排序且穩定的佇列。

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0  # 用來記錄插入順序，避免同優先級時無法比較 item

    def push(self, item, priority):
        # heapq 是 min-heap；放入 -priority 後就能模擬 max-heap（優先級高者先出）
        # tuple 比較規則：先比 -priority，再比 _index，最後才比 item
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # 取出 tuple 的最後一個元素，也就是原本存入的 item
        return heapq.heappop(self._queue)[-1]
