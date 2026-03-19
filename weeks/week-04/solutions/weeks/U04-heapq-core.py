# U4. heap 為何能高效拿 Top-N（1.4）

import heapq

nums = [5, 1, 9, 2]

# 先複製一份，避免修改原列表
h = nums[:]

# 將列表轉成「最小堆」
heapq.heapify(h)

# heap 的核心性質：
#   h[0] 永遠是整個 heap 中的最小值
#   （因為 heap 是一棵「部分排序」的二元樹）
h[0]   # → 1

# heappop() 會彈出目前最小的元素，並維持 heap 結構
m = heapq.heappop(h)   # → 1