# R5. 優先佇列 PriorityQueue（1.5）

import heapq

class PriorityQueue:
    def __init__(self):
        # _queue: 儲存堆資料；_index: 同優先權時維持插入順序
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # heapq 是最小堆，將 priority 取負可達到「優先權越大越先出」
        # 加入 _index 作為第二排序鍵，避免 item 之間不可比較
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # 取出堆頂元素，回傳原始 item
        return heapq.heappop(self._queue)[-1]
