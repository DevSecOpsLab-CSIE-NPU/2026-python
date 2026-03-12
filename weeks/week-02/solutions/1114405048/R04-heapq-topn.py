# R04 heapq top-n
# 目標：示範 heapq 的 nlargest / nsmallest 與 heapify。

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 取最大的 3 個值
largest_3 = heapq.nlargest(3, nums)
# 取最小的 3 個值
smallest_3 = heapq.nsmallest(3, nums)

portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "AAPL", "shares": 50, "price": 543.22},
]

# key 參數可指定比較欄位
cheapest = heapq.nsmallest(1, portfolio, key=lambda s: s["price"])

# 將 list 原地轉成 min-heap
heap = list(nums)
heapq.heapify(heap)
smallest = heapq.heappop(heap)
