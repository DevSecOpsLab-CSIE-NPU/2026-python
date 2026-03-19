"""
U04: heapq 的基本概念

Python 的 heapq 是最小堆。
"""

import heapq


nums = [5, 1, 9, 2]
h = nums[:]
heapq.heapify(h)

# h[0] 會是目前最小的值。
m = heapq.heappop(h)
