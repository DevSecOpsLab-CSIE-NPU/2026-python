"""R04: heapq 取得 Top-N / Bottom-N。"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print('最大 3 個:', heapq.nlargest(3, nums))
print('最小 3 個:', heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
]

cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
print('最便宜的 2 檔:', cheap)

# 將 list 原地轉成 heap
heap = list(nums)
heapq.heapify(heap)
print('heap 首元素(最小值):', heap[0])
print('heappop 取出最小值:', heapq.heappop(heap))
