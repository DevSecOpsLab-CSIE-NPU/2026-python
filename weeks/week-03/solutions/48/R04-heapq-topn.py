# R4. heapq 取 Top-N（1.4）

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# 取出最大的 3 個值
heapq.nlargest(3, nums)
# 取出最小的 3 個值
heapq.nsmallest(3, nums)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]
# 可搭配 key 指定比較欄位，這裡找價格最低的項目
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

# 原地轉為最小堆（min-heap）
heap = list(nums)
heapq.heapify(heap)
# 每次彈出目前最小值
heapq.heappop(heap)
