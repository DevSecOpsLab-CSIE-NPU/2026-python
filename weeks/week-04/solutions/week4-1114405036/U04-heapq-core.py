# U4. heap 為何能高效拿 Top-N（1.4）
# 說明：堆積 (Heap) 是一種資料結構，其根節點 (h[0]) 永遠是最小（或最大）值。

import heapq

nums = [5, 1, 9, 2, 7, 3]
h = nums[:]

# 1. 將 list 轉換為 heap 結構 (in-place)
# 這是一個效率很高的操作，時間複雜度為 O(N)
heapq.heapify(h)

# 2. h[0] 永遠是最小值
print(f"最小值是: {h[0]}") # 1

# 3. 每次彈出 (pop) 都會拿到當前最小的元素，並自動重整
min_val = heapq.heappop(h) # 拿走 1，剩下裡面最小的是 2