# U4. heap 為何能高效拿 Top-N（1.4）

import heapq

nums = [5, 1, 9, 2]
h = nums[:]
heapq.heapify(h)
# h[0] 永遠是最小值（這是 heap 的核心性質）
m = heapq.heappop(h)  # 每次 pop 都拿到目前最小
