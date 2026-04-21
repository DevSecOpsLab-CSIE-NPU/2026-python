# U04 heapq 核心概念
# 重點：Python 的 heapq 是「最小堆」，最小值永遠在索引 0。

import heapq

nums = [5, 1, 9, 2]
h = nums[:]

# 原地轉成 heap 結構（不是完整排序）。
heapq.heapify(h)

# 每次 heappop 都會彈出當前最小值。
m = heapq.heappop(h)
