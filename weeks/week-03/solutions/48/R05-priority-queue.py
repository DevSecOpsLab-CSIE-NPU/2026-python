# R5. 優先佇列 PriorityQueue（1.5）

import heapq

class PriorityQueue:
    def __init__(self):
        # 內部使用 heapq 儲存 (優先序, 插入序, 物件)
        self._queue = []
        # 用來維持同優先序時的先進先出
        self._index = 0
    def push(self, item, priority):
        # heapq 是最小堆，因此用負號把數值大的 priority 排在前面
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        # 取出 tuple 的最後一格，也就是原始 item
        return heapq.heappop(self._queue)[-1]
