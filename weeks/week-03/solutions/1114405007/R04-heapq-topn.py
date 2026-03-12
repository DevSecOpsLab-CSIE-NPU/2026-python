# R4: heapq 與 Top-N 問題
# 觀念：heapq 提供最小堆（min-heap），可快速找出前 N 大/前 N 小。

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 取出前 3 大、前 3 小（不改動原串列）
heapq.nlargest(3, nums)
heapq.nsmallest(3, nums)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]

# 依照 price 欄位找出最便宜的 1 筆
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

# heapify 會把一般 list 原地轉成最小堆結構
heap = list(nums)
heapq.heapify(heap)
# heappop 每次彈出目前最小值
heapq.heappop(heap)
