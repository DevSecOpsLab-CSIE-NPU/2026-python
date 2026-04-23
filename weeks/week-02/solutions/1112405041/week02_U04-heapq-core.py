# 【Bloom 階段：U - 理解與進階應用】
# U4. Heap 的最小元素性質
# August 的惡意提醒：heapify 之後，heap[0] 雖然「保證」是最小元素，
# 但 heap[1] 並不保證是第二小！要依序拿最小值，必須使用 heappop。
# 誤以為 heap 是一個完整的有序列表，是常見的效能雷來源。

import heapq

nums = [5, 1, 9, 2]
h = nums[:]
heapq.heapify(h)

# heap[0] 永遠是最小值 (最小堆的屬性)
print(f"Current Min (h[0]): {h[0]}")

# 逐一取出最小值，heappop 會自動重新調整堆 (O(log N))
while h:
    m = heapq.heappop(h)
    print(f"Popped Min: {m}")

# August 惡意筆記：若要一次拿前 N 名，nlargest/nsmallest 更快；
# 若要一個一個處理權重，heappop 是正解。
