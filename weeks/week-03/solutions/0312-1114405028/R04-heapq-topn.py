# R4. heapq 取 Top-N（1.4）
# nlargest/nsmallest 可用於數值或複雜結構。

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print("原始數列", nums)
print("3 個最大值", heapq.nlargest(3, nums))
print("3 個最小值", heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]
print("最低價格股票", heapq.nsmallest(1, portfolio, key=lambda s: s['price']))

# 將任意列表原地轉為堆，然後 pop 出最小值
heap = list(nums)
heapq.heapify(heap)
print("heapify 後", heap)
print("heappop gives", heapq.heappop(heap))
