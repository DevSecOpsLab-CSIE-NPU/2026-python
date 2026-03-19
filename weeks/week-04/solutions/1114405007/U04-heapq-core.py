# U4. heap 為何能高效拿 Top-N（1.4）

import heapq

nums = [5, 1, 9, 2]

# 先複製一份，避免直接改動原始串列
h = nums[:]

# 原地轉成最小堆積（min-heap）
heapq.heapify(h)

# h[0] 永遠是最小值（這是 heap 的核心性質）
m = heapq.heappop(h)  # 每次 pop 都拿到目前最小
print('原始串列:', nums)
print('heapify 後:', h)
print('pop 最小值:', m)
print('剩餘 heap:', h)
