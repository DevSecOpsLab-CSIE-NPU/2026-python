# R5. 優先佇列 PriorityQueue（1.5）

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

# 數字越大優先權越高
pq = PriorityQueue()
pq.push('低優先工作', 1)
pq.push('高優先工作', 5)
pq.push('中優先工作', 3)

print('第 1 次 pop:', pq.pop())
print('第 2 次 pop:', pq.pop())
print('第 3 次 pop:', pq.pop())
