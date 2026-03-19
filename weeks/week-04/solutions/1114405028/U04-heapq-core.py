# U4. heap 為何能高效拿 Top-N（1.4）

import heapq  # heapq：最小堆積（min-heap）模組，所有操作 O(log n)

nums = [5, 1, 9, 2]
h = nums[:]          # 複製一份，不破壞原始資料
heapq.heapify(h)     # 原地將 list 重新排列成 heap 結構，時間複雜度 O(n)
# h[0] 永遠是最小元素（這是 heap 的核心性質）
m = heapq.heappop(h) # heappop：移除並回傳最小元素，heap 自動重新平衡 O(log n)
                     # 若要取 Top-N 最大，改用 heapq.nlargest(n, nums)
