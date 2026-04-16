# R4. heapq 取 Top-N（1.4）

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.nlargest(3, nums)
heapq.nsmallest(3, nums)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

heap = list(nums)
heapq.heapify(heap)
heapq.heappop(heap)
