"""
R05: 自製 Priority Queue

這個範例用 heapq 包裝出「優先權越高越先出列」的佇列。
"""

import heapq


class PriorityQueue:
    """以 heapq 實作的優先佇列（高 priority 先出列）。"""

    def __init__(self):
        # _queue 內部儲存堆資料；_index 用來打破同優先權時的平手。
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # heapq 是最小堆，因此把 priority 取負號，
        # 就能把「數值較大的 priority」排到前面。
        # tuple 第二欄放 _index，可確保同優先權時維持先進先出（穩定排序）。
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # 取出堆頂元素，回傳原始 item（tuple 最後一欄）。
        return heapq.heappop(self._queue)[-1]
