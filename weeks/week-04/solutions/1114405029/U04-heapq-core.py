# U4. heap 為何能高效拿 Top-N（1.4）

# 匯入 heapq 模組
# heapq 是 Python 提供的堆積（heap）工具
# 它可以把串列整理成「最小堆積（min-heap）」
# 最小堆積的核心特性是：最小值永遠會放在索引 0 的位置
import heapq

# 建立一個普通串列 nums
# 這裡面有 4 個數字，順序目前是一般串列順序，還不是 heap 結構
nums = [5, 1, 9, 2]

# 使用切片 nums[:] 複製出一份新的串列給 h
# 這樣做的目的是保留原本的 nums 不被修改
# 後續我們會把 h 轉成 heap
h = nums[:]

# 使用 heapify() 將普通串列 h 原地轉換成 heap 結構
# 注意：轉換後的串列看起來不一定是完整排序好的，
# 但它一定會符合 heap 的規則：
# 最小值會在 h[0]，而且父節點會小於等於子節點
heapq.heapify(h)

# h[0] 永遠是最小值（這是 heap 的核心性質）

# 使用 heappop() 從 heap 中取出最小值
# 取出後，heap 會自動重新調整結構，讓新的最小值繼續放在 h[0]
# 因此 heappop() 每執行一次，都能高效率地拿到「目前最小值」
m = heapq.heappop(h)  # 每次 pop 都拿到目前最小

# 印出原始串列 nums
print("原始串列 nums：", nums)

print()  # 空一行，讓輸出結果更清楚

# 印出經過 heapify() 後的 h
# 注意：這不一定會是完全排序後的結果
# 但一定符合最小堆積的規則
print("經過 heapify() 轉成 heap 後的 h：", h)

# 印出目前 heap 最前面的元素
# 因為 heap 的特性，h[0] 一定是目前最小值
print("heap 的最小值 h[0]：", h[0])

print()  # 空一行，讓輸出結果更清楚

# 印出使用 heappop() 取出的最小值
print("使用 heappop() 取出的最小值 m：", m)

# 印出取出最小值之後，heap 剩下的內容
# 此時 h 仍然會維持 heap 結構
print("取出最小值後，剩下的 heap h：", h)

print()  # 空一行，讓輸出結果更清楚

# 補充說明 heap 為什麼適合拿 Top-N
print("說明：heap 會把最小值維持在最前面，因此可以快速取得目前最小值。")
print("每次 heappop() 取出最小值後，heap 也會自動重新整理。")
print("因此在需要反覆取出最小值或最大值（Top-N 問題）時，效率會比每次重新排序更好。")