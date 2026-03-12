"""
R04: heapq 與 Top-N

heapq 提供最小堆（min-heap）操作，常用在 Top-N 與優先處理場景。
"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 直接取得最大的 3 個值。
heapq.nlargest(3, nums)

# 直接取得最小的 3 個值。
heapq.nsmallest(3, nums)

portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "AAPL", "shares": 50, "price": 543.22},
]

# 透過 key 指定比較欄位，找出價格最低的一筆。
heapq.nsmallest(1, portfolio, key=lambda s: s["price"])

# 先把一般 list 轉成堆結構（原地轉換）。
heap = list(nums)
heapq.heapify(heap)

# heappop 每次都會彈出「目前最小值」。
heapq.heappop(heap)
