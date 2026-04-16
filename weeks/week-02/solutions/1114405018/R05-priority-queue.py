"""R5. 優先佇列 PriorityQueue（1.5）

優先佇列（Priority Queue）是一種「依優先權取出元素」的資料結構。
這個版本用 heapq 實作，重點是：
1. priority 數值越大，表示優先權越高。
2. heapq 預設是最小堆，所以要用負號把高優先權變成較小的值。
3. 用 index 當平手時的第二排序鍵，讓插入順序可預測。
"""

import heapq


class PriorityQueue:
    def __init__(self):
        # _queue 儲存堆積資料；_index 用來記錄插入順序
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # heapq 是最小堆，因此用 -priority 讓 priority 越大的元素越先被取出
        # _index 用來避免 priority 相同時比較 item 本身造成錯誤
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heappop() 回傳 tuple，最後一個元素才是原本放進去的 item
        return heapq.heappop(self._queue)[-1]
