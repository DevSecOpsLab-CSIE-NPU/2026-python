"""R05: 用 heapq 實作簡易優先佇列。"""

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # priority 越大越先出列，故使用負號反轉
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


pq = PriorityQueue()
pq.push('low', priority=1)
pq.push('high', priority=5)
pq.push('medium', priority=3)

print('pop #1:', pq.pop())
print('pop #2:', pq.pop())
print('pop #3:', pq.pop())
