# R4. heapq 取 Top-N（1.4）

import heapq

# 一般數字列表
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 取出最大 3 個值（回傳列表，已排序）
heapq.nlargest(3, nums)     # → [42, 37, 23]

# 取出最小 3 個值
heapq.nsmallest(3, nums)    # → [-4, 1, 2]

# 也可以搭配 key 參數，從複雜資料結構中取 Top-N
portfolio = [
    {'name': 'IBM',  'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50,  'price': 543.22},
]

# 取出價格最低的 1 筆（依 price 排序）
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

# 將 nums 轉成 heap（最小堆）
heap = list(nums)
heapq.heapify(heap)   # 將列表原地轉換成 heap 結構

# heappop() 會彈出最小的元素（因為是最小堆）
heapq.heappop(heap)