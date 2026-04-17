# R4. heapq 取 Top-N（1.4）
# =========================================================
# heapq 模組提供了堆積佇列算法（Heap Queue Algorithm）的實現
# Python 的 heapq 實現的是最小堆（Min Heap），根節點是最小值
# 堆是一種特殊的完全二叉樹資料結構，用於高效排序和優先級隊列
# =========================================================

import heapq

# 數字列表
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# nlargest(n, iterable): 返回最大的 n 個元素（保持原順序）
# 返回：[42, 37, 23]
heapq.nlargest(3, nums)

# nsmallest(n, iterable): 返回最小的 n 個元素（保持原順序）
# 返回：[-4, 1, 2]
heapq.nsmallest(3, nums)

# 使用 key 參數指定排序依據（適用於複雜物件）
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]

# 返回價格最低的1筆資料（列表）
# 結果：[{'name': 'IBM', 'shares': 100, 'price': 91.1}]
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

# heapify(): 將列表原地轉換為堆結構（O(n)時間複雜度）
# 轉換後的列表仍可正常索引，但堆的性質是 parents <= children
heap = list(nums)
heapq.heapify(heap)

# heappop(): 彈出並返回堆中最小的元素，同時維持堆結構
# 每次彈出後，堆會自動重組
heapq.heappop(heap)
