"""U04: heapq 的核心是最小堆，不是排序後清單。"""

import heapq

nums = [5, 1, 9, 2]
h = nums[:]
heapq.heapify(h)

print('heapify 後:', h)
print('h[0] 一定是最小值:', h[0])
print('heappop #1:', heapq.heappop(h))
print('heappop #2:', heapq.heappop(h))
print('剩餘 heap:', h)
