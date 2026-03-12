# R4. heapq 取 Top-N（1.4）

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
largest3 = heapq.nlargest(3, nums)
smallest3 = heapq.nsmallest(3, nums)
print('最大的 3 個數:', largest3)
print('最小的 3 個數:', smallest3)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]
cheapest = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])[0]
print('價格最低的股票資料:', cheapest)

heap = list(nums)
heapq.heapify(heap)
first_pop = heapq.heappop(heap)
print('heapify 後先彈出的最小值:', first_pop)
print('目前 heap 前幾個元素:', heap[:5])
