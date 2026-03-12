# R05 priority queue
# 目標：以 heapq 實作簡易優先佇列（priority 越大越先出列）。

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # heapq 是 min-heap，因此用負號把大 priority 轉成小數值。
        # _index 用來保證同優先級時仍維持插入順序。
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
