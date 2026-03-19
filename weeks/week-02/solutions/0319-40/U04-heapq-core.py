# U4. heap 為何能高效拿 Top-N（1.4）

import heapq

nums = [5, 1, 9, 2]
h = nums[:]
heapq.heapify(h)

print("原始 nums =", nums)
print("heapify 後 h =", h)
print("h[0]（最小值）=", h[0])

m = heapq.heappop(h)
print("heappop 拿到 =", m)
print("pop 後 h =", h)
