# R4. heapq 取 Top-N（1.4）

import heapq

# ── 1. 基礎數值取 Top-N ──────────────────────────────
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# nlargest(n, iterable)：從序列中找出最大的前 n 個元素
# 結果：[42, 37, 23]
heapq.nlargest(3, nums)

# nsmallest(n, iterable)：從序列中找出最小的前 n 個元素
# 結果：[-4, 1, 2]
heapq.nsmallest(3, nums)

# ── 2. 處理複雜結構（如字典列表） ────────────────────
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
]

# 透過 key 參數指定比較基準（使用 lambda 匿名函式）
# 此處以 'price' (價格) 為準，找出最便宜的一筆資料
# 結果：[{'name': 'FB', 'shares': 200, 'price': 21.09}]
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

# ── 3. 底層堆疊操作 ──────────────────────────────────
# 複製原始數據，並將其轉換成一個列表
heap = list(nums)

# heapify(x)：將列表「原地」(In-place) 轉換為最小堆疊 (Min-Heap)
# 轉換後，heap[0] 必定是最小元素。時間複雜度為 O(N)
heapq.heapify(heap)

# heappop(x)：彈出並回傳堆疊中的最小元素
# 剩餘的堆疊會自動重新調整，維持「最小元素在最上方」的特性
# 時間複雜度為 O(log N)
heapq.heappop(heap)