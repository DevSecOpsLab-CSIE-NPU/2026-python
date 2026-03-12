# R5. 優先佇列 PriorityQueue（Implementing a Priority Queue）—— Python Cookbook 1.5

import heapq

class PriorityQueue:
    """以 heapq 實作的優先佇列：priority 越高的項目越優先被取出"""

    def __init__(self):
        self._queue = []   # 儲存 (-priority, index, item) 三元組的 heap
        self._index = 0    # 插入序號，用來打破相同 priority 時的平手

    def push(self, item, priority):
        # heapq 是最小堆（min-heap），取出的是最小值
        # 將 priority 取負數，讓「數值最大的 priority」變成「heap 中最小的數」
        # _index 確保相同 priority 時，先插入的先出（FIFO）
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heappop 取出 (-priority, index, item) 三元組中最小的那個
        # 也就是 priority 最高的項目
        # [-1] 取出 item（忽略 priority 和 index）
        return heapq.heappop(self._queue)[-1]

# 使用範例：
# pq = PriorityQueue()
# pq.push('低優先任務', 1)
# pq.push('高優先任務', 5)
# pq.pop()  → '高優先任務'
