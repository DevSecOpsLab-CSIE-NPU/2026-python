# R4. heapq 取 Top-N（1.4）
#
# heapq 提供堆積結構，常用在：
# 1. 快速找出最大/最小的前 N 筆資料。
# 2. 對資料做最小堆操作，維持部分排序。
# 3. 搭配 key 參數時，可以依照指定欄位排序取值。

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
