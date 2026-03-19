# U4. heap 為何能高效拿 Top-N（1.4）
# 展示使用堆（heap）結構對數字列表進行高效排序和選擇

# 導入 heapq 模組進行堆操作
import heapq

# 原始數字列表
nums = [5, 1, 9, 2]

# 複製列表以保留原始資料
h = nums[:]

# 將列表轉換為堆結構
# heapify 重新整理列表成最小堆（min heap）
heapq.heapify(h)  # 堆現在滿足性質：父節點 ≤ 子節點
# 結果：h 現在變成類似 [1, 2, 9, 5] 的結構

# 堆的核心性質：根元素（h[0]）永遠是最小值
print(f"堆的最小元素 h[0]: {h[0]}")  # 1（目前的最小值）

# 移除並返回堆中的最小元素
print(f"原始堆: {h}")
m = heapq.heappop(h)  # 返回 1，堆重新調整
print(f"第 1 次 heappop: {m}, 剩餘堆: {h}")

# 再調用一次 heappop 會返回後續最小值
print(f"\n依序取出最小元素:")
while h:
    val = heapq.heappop(h)
    print(f"取出: {val}")
# 這樣就能依序拿到最小的 N 個元素，時間複雜度為 O(N log N)
