# R5. 優先佇列 PriorityQueue（1.5）

import heapq

class PriorityQueue:
    def __init__(self):
        # _queue 用來存放 heap 的內容（內部使用最小堆）
        self._queue = []
        # _index 用來確保相同 priority 時仍能依插入順序排序
        self._index = 0

    def push(self, item, priority):
        # heappush() 會把元素放入最小堆
        # 為了讓「priority 越大越優先」，這裡把 priority 取負值
        # 存入格式：(-priority, index, item)
        # index 確保當 priority 相同時，先插入的先被彈出（穩定排序）
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heappop() 會彈出最小的元素（因為是最小堆）

        return heapq.heappop(self._queue)[-1]