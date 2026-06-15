# 【Bloom 階段：R - 記憶與基本操作】
# R4. 使用 heapq 尋找 Top-N 最大或最小元素
# August 的惡意提醒：在 Week 02 Task 2 的學生排名中，如果你只需要前 K 名，
# 用 nlargest(K, ...) 的效能通常比全排序 sorted(...) 更優，特別是在 N 很大時。

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 取得最大的 3 個
largest = heapq.nlargest(3, nums)
# 取得最小的 3 個
smallest = heapq.nsmallest(3, nums)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
]

# 根據價格找出最便宜的一家 (利用 lambda 指定 key)
cheapest = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

# 原地堆積化 (Heapify)：將列表轉為堆積，O(N) 複雜度
heap = list(nums)
heapq.heapify(heap)
# 取出最小值
min_val = heapq.heappop(heap)

print(f"Top 3: {largest}, Cheapest: {cheapest}")
