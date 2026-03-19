# U4. heap 為何能高效拿 Top-N（1.4）
#
# 觀念重點：
# - Python 的 heapq 是「最小堆」（min-heap）。
# - 堆的核心保證是 h[0] 永遠是目前最小值。
# - heappop 每次都能在 O(log n) 取出最小值。

import heapq

nums = [5, 1, 9, 2]

# 複製一份資料，避免直接改到原陣列。
h = nums[:]

# 就地轉成 heap 結構（heapify 複雜度約 O(n)）。
heapq.heapify(h)

# h[0] 永遠是最小值（這是 heap 的核心性質）。

# 每次 pop 都取出「目前最小」元素。
m = heapq.heappop(h)
