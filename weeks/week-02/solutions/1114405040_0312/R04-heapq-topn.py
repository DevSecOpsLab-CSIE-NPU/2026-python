# R4. heapq 取 Top-N（Finding the Largest/Smallest N Items）—— Python Cookbook 1.4

import heapq

# ── nlargest / nsmallest ─────────────────────────────────
# heapq.nlargest(n, iterable)  → 回傳最大的 n 個元素（由大到小排列）
# heapq.nsmallest(n, iterable) → 回傳最小的 n 個元素（由小到大排列）
# 內部使用 heap，比 sorted() 整體排序再切片更有效率（當 N << 總數量時）
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.nlargest(3, nums)   # [42, 37, 23]
heapq.nsmallest(3, nums)  # [-4, 1, 2]

# ── 搭配 key 函式：對字典列表排序 ──────────────────────────
# key=lambda s: s['price'] 指定「比較依據」為 price 欄位
# 取出 price 最低的 1 筆（最便宜的公司）
portfolio = [
    {'name': 'IBM',  'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50,  'price': 543.22},
]
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
# 回傳 [{'name': 'IBM', 'shares': 100, 'price': 91.1}]

# ── 手動建 heap 並逐步取最小值 ───────────────────────────
# heapify 將 list 就地變成最小堆（min-heap），O(n)
# heappop  每次取出並移除最小值，O(log n)
heap = list(nums)
heapq.heapify(heap)   # 原地轉為 heap，heap[0] 永遠是最小值
heapq.heappop(heap)   # 取出並移除最小值（-4），heap 自動重新排列
