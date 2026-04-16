# R5. 優先佇列 PriorityQueue（1.5）
#
# 這個版本用 heapq 實作優先佇列：
# 1. priority 數字越大，代表優先權越高。
# 2. 內部把 priority 取負號，讓 heapq 能模擬「最大優先」。
# 3. 加上 _index 可以確保 priority 相同時，仍保留先進先出順序。

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
