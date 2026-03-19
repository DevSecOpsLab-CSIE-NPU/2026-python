# U4. heap 為何能高效拿 Top-N（1.4）
"""
本範例示範 Python 的 heapq 模組（最小堆）如何用於高效地取得 Top-N（最小/最大）值。

堆（heap）是一種完全二元樹（complete binary tree），支援快速取得最小值或最大值。
Python 的 heapq 實作為「最小堆」，其核心性質是:
- heap[0] 永遠是目前所有元素中的最小值

堆的操作時間複雜度通常為 O(log n)，比排序後再取前 N 筆更有效率（O(n log n)）。
"""

import heapq

# 範例資料
nums = [5, 1, 9, 2]

# heapify 會原地將 list 轉換成 heap 結構（最小堆）
# 它的時間複雜度為 O(n)
h = nums[:]
heapq.heapify(h)

# heap 的核心性質：h[0] 永遠是最小值
# 下面的 heappop 會彈出並回傳目前的最小值
m = heapq.heappop(h)  # 每次 pop 都拿到目前最小

# 如果要取得前 N 小的元素，可以連續呼叫 heappop N 次，
# 或使用 heapq.nsmallest / heapq.nlargest 取得 Top-N。

