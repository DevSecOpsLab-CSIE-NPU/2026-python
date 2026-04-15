# U4. heap 為何能高效拿 Top-N（1.4）

# heap（堆）是一種二元樹結構，在記憶體中以陣列形式表示。
# 核心性質：
# - min heap：父節點 ≤ 子節點（parent <= left, right）
# - 因此根節點（索引 0）永遠是最小值
# - 這個性質使得快速存取最小值變得可能

import heapq

# 原始無序列表。
nums = [5, 1, 9, 2]

# 建立一個淺複本，稍後用 heapify 轉成 heap。
h = nums[:]
print(h)  # 原始列表未排序，輸出 [5, 1, 9, 2]

# heapify 將列表平地轉換成 heap 結構（in-place，O(n) 時間）。
# 轉換後的 h 會滿足 min heap 性質，但「不是完全排序的」。
heapq.heapify(h)

# heap 的結構保證：h[0] 永遠是最小值（這是 heap 的核心性質）
# 此時 h[0] 會是 1，儘管整個列表未完全排序。

# heappop 移除並回傳最小元素（O(log n) 時間）。
# 移除後，heapq 自動重新調整堆結構，保持最小值在 h[0]。
m = heapq.heappop(h)  # 每次 pop 都拿到目前最小
print(m, h)  # 最小值=1, 剩餘 heap 為 [2, 5, 9]

# 為何 heap 能高效拿 Top-N？
# - 若要找所有資料中最小的 N 筆：
#   - 用排序：O(n log n) 時間
#   - 用 heappop N 次：O(n + N log n) 時間
#   - 當 N << n 時，heap 方式更高效
#
# - 常見應用：
#   - 優先佇列
#   - Dijkstra 最短路徑算法
#   - Top-K 最頻繁元素
#   - 堆排序（全排序時 O(n log n)）

# 補充：Python 的 heapq 內建是 min heap。
# 若需要 max heap，可將值取負後再放入。

