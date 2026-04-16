"""
U4. heap 為何能高效拿 Top-N（1.4）

功能：演示最小堆（min heap）的核心性質

核心概念：
  - heap：堆，一種特殊的二叉樹結構
  - min heap：最小堆，根節點最小
  - max heap：最大堆，根節點最大
  - Python heapq 默認實現最小堆

關鍵特徵：
  1. h[0] 總是最小元素 ✓
  2. 不是完全排序（只有最小的元素保證在頂部）
  3. 添加/移除的時間複雜度：O(log n)
  4. 查詢最小值：O(1)
  5. 完美用於 Top-N 問題

應用場景：
  - 實時找出最小的 N 個數
  - 優先級隊列（優先處理優先級最高的任務）
  - 定時器隊列（執行最近要執行的任務）
  - 成本最小的路徑（Dijkstra 算法）
"""

import heapq
"""
導入 heapq 模塊

說明：
  - heapq：Python 標準庫的堆隊列模塊
  - 實現了 min-heap（最小堆）
  - 是一個二叉堆實現
  
主要函數：
  - heapify()：將列表原地轉換為堆
  - heappush()：向堆中添加元素
  - heappop()：移除並返回最小元素
  - heappushpop()：先 pop 後 push
  - heapreplace()：先 push 後 pop
  - nlargest(n, iterable)：找 n 個最大的
  - nsmallest(n, iterable)：找 n 個最小的
"""

# ════════════════════════════════════════════════════════
# 堆的基本操作
# ════════════════════════════════════════════════════════

nums = [5, 1, 9, 2]
"""
原始列表（普通列表，沒有堆的性質）

元素分析：
  - 5（索引 0）
  - 1（索引 1）
  - 9（索引 2）
  - 2（索引 3）

說明：
  - 這只是一個普通的無序列表
  - 還不是堆結構
"""

h = nums[:]
"""
創建一個副本

操作說明：
  h = nums[:] 創建淺複製
  
為什麼需要副本？
  1. 保持原列表不變
  2. 原列表可能還有其他用途
  3. heapify() 進行原地修改
  
h 現在：[5, 1, 9, 2]（與 nums 相同，但是獨立副本）
"""

heapq.heapify(h)
"""
將列表轉換為堆結構（最小堆）

操作說明：
  heapq.heapify(h) 進行原地修改
  
執行過程（內部）：
  1. 從最後一個非葉節點開始
  2. 逐個進行「下沉」操作
  3. 確保滿足堆的性質：父節點 ≤ 子節點
  
時間複雜度：
  - heapify()：O(n)
  - 比逐個 push：O(n log n) 快得多！

heapify 後的狀態（可視化）：

原始：[5, 1, 9, 2]

轉換為二叉樹表示：
  原始結構：
       5
      / \\
     1   9
    /
   2

  heapify 後（最小堆）：
       1
      / \\
     2   9
    /
   5

  索引對應：
    h = [1, 2, 9, 5]
    
  堆的性質驗證：
    - h[0] = 1（根節點，最小）✓
    - h[0] ≤ h[1]：1 ≤ 2 ✓
    - h[0] ≤ h[2]：1 ≤ 9 ✓
    - h[1] ≤ h[3]：2 ≤ 5 ✓

索引關係（重要！）：
  對於索引 i 的節點：
    - 父節點：(i-1) // 2
    - 左子節點：2*i + 1
    - 右子節點：2*i + 2

驗證示例：
  node_index=1（值 2）：
    - 父節點索引：(1-1)//2 = 0（值 1）✓
    - 左子節點索引：2*1+1 = 3（值 5）✓

重要特性：
  - 堆是「部分有序」的，不是完全排序
  - 只保證最小值在根節點
  - 子樹可能無序

vs 完全排序的區別：

完全排序（sorted）：
  [1, 2, 5, 9]
  - 所有元素有序
  - 構建時間：O(n log n)
  - 查詢任意位置：O(1)
  - 添加新元素：O(n)（需要重新排序）

弱排序（堆）：
  [1, 2, 9, 5]
  - 只保證最小值在頂
  - 構建時間：O(n)
  - 查詢最小值：O(1)
  - 添加新元素：O(log n)✓ 高效

選擇建議：
  - 只需最小值 → 用堆 ✓
  - 需要完全有序 → 用 sort
"""

# h[0] 永遠是最小值（這是 heap 的核心性質）
"""
堆的核心保證：h[0] 總是最小元素

為什麼這是真的？

原因：
  heapify() 過程確保了「堆的性質」
  → min-heap 性質：parent ≤ children

推論：
  - 根節點 h[0] 是整個樹的最小值
  - 無論何時操作 h，這個性質都保持
  - 這就是「不變量」（invariant）

驗證示例：
  h = [1, 2, 9, 5]（heapify 後）
  
  檢查所有父子關係：
    h[0]=1 與子節點 h[1]=2：1 ≤ 2 ✓
    h[0]=1 與子節點 h[2]=9：1 ≤ 9 ✓
    h[1]=2 與子節點 h[3]=5：2 ≤ 5 ✓
  
  因此 h[0]=1 必然是整體最小值 ✓

時間複雜度：
  - 查詢最小值（h[0]）：O(1)✓ 常數時間
  - vs sorted 列表 sorted[0]：也是 O(1)
  - vs 線性搜索找最小值：O(n)
  
  堆的優勢：
    - 查詢最小值快（O(1)）
    - 添加/移除也快（O(log n)）
    - 總時間複雜度更優
"""

m = heapq.heappop(h)  # 每次 pop 都拿到目前最小
"""
從堆中取出最小元素（並移除）

操作說明：
  heappop(h) 執行兩個步驟：
    1. 返回最小元素（h[0]）
    2. 移除該元素（並重新組織堆）

執行過程詳解：

步驟1：記錄最小值
  m = h[0] = 1

步驟2：移除根節點
  原堆：
       1
      / \\
     2   9
    /
   5
  
  移除 1 後變成：
       ?
      / \\
     2   9
    /
   5

步驟3：重新調整堆
  策略：把最後一個元素（5）移到根
       5
      / \\
     2   9
  
  問題：5 > 2，違反了堆的性質！
  
步驟4：「下沉」操作
  5 與較小的子節點交換
       2
      / \\
     5   9
  
  現在 h = [2, 5, 9]

檢查堆的性質：
  h[0]=2 ≤ h[1]=5 ✓
  h[0]=2 ≤ h[2]=9 ✓
  堆的性質保持 ✓

結果：
  m = 1（返回值）
  h = [2, 5, 9]（更新後的堆）

時間複雜度：
  heappop()：O(log n)
  - 下沉操作最多進行 log n 次
  - 堆的高度是 log n

連續 pop 演示：

初始堆：[1, 2, 9, 5]

第 1 次 pop：
  移除 1，重新調整
  h = [2, 5, 9]

第 2 次 pop：
  移除 2，重新調整
  h = [5, 9]

第 3 次 pop：
  移除 5，重新調整
  h = [9]

第 4 次 pop：
  移除 9
  h = []

全部移除順序（最小堆）：
  1 → 2 → 5 → 9
  完全按升序排列！

重要觀察：
  - 逐個 pop 的結果是完全排序
  - 但構建堆只需 O(n)
  - 總時間：O(n + n log n) = O(n log n)
  - 與排序相同，但可以提前退出（Top-N 場景）
"""


# ════════════════════════════════════════════════════════
# Top-N 問題（堆的最主要應用）
# ════════════════════════════════════════════════════════

"""
堆的經典應用：快速找出最小/最大的 N 個元素

場景1：從百萬數據中找出最小的 10 個

方案A：完全排序（不推薦）
  sorted_nums = sorted(nums)  # O(n log n)
  top_10 = sorted_nums[:10]   # 取前 10 個
  
  問題：
    - 對所有元素排序很浪費
    - 只需要 10 個，其他 999990 個排序無用

方案B：堆（推薦）✓
  h = nums[:]
  heapq.heapify(h)            # O(n)
  top_10 = [heapq.heappop(h) for _ in range(10)]  # O(10 log n)
  
  總時間：O(n + 10 log n) ≈ O(n)✓
  
  優勢：
    - 堆化只需 O(n)
    - 幾乎不排序就得到結果！

場景2：找最大的 N 個元素

Python heapq 只有 min-heap
→ 負數技巧（所有數取負）：

  nums = [5, 1, 9, 2]
  neg_nums = [-x for x in nums]  # [-5, -1, -9, -2]
  
  h = neg_nums[:]
  heapq.heapify(h)               # [[-9, -5, -1, -2]]
  
  # 最小堆中最小的 = 原最大的
  largest = [-heapq.heappop(h) for _ in range(2)]
  # [9, 5]

或者用內置函數（更简單）：
  import heapq
  largest = heapq.nlargest(2, nums)  # [9, 5]
  smallest = heapq.nsmallest(2, nums)  # [1, 2]

時間複雜度對比：

問題：從 N=100 萬個數中找 K=10 個最小的

方案1：sorted()
  時間：O(n log n) = O(100萬 × 20) ≈ 2000 萬次操作

方案2：heapq
  時間：O(n + k log n) = O(100萬 + 10 × 20) ≈ 100萬 次操作 ✓
  
  性能提升：20倍! 🚀

方案3：heapq.nsmallest() 或 heapq.nlargest()
  內部優化更好，推薦使用

堆排序的完整例子：

  def heap_sort(nums):
      h = nums[:]
      heapq.heapify(h)                    # O(n)
      return [heapq.heappop(h) for _ in range(len(nums))]  # O(n log n)
  
  result = heap_sort([5, 1, 9, 2])
  # [1, 2, 5, 9]
  
  時間複雜度：O(n log n) 與 sorted 相同
  但可以提前終止（Top-N）✓

實際應用：

應用1：實時找最低的 N 個價格
  prices = deque(maxlen=1000)  # 保留最近 1000 個價格
  
  def get_best_prices(n):
      return heapq.nsmallest(n, prices)
  
  # 常數級查詢，非常快

應用2：優先級隊列
  import heapq
  
  tasks = []  # Min-heap
  
  def add_task(priority, task):
      heapq.heappush(tasks, (priority, task))
  
  def get_next_task():
      return heapq.heappop(tasks)  # 總是取最高優先級
  
  # 醫院掛號系統：
  #   VIP 患者 priority=1
  #   普通患者 priority=10
  #   緊急患者 priority=0（最先看）

應用3：Dijkstra 最短路徑算法
  使用堆來快速找出最小成本的節點
  時間複雜度從 O(n²) 降至 O((n+m) log n)

堆的其他操作：

1. 添加元素
   heapq.heappush(h, new_element)  # O(log n)
   
   示例：
   h = [1, 2, 9, 5]
   heapq.heappush(h, 0)
   # h = [0, 1, 9, 5, 2]（重新平衡）

2. 替換最小元素
   heapq.heapreplace(h, new_element)
   # = heappop() + heappush()
   # 但更高效
   
3. 原地替換並保持 heap 性質
   heapq.heappushpop(h, item)

常見陷阱：

陷阱1：混淆 min-heap 和 max-heap
  Python heapq 是 min-heap
  h[0] 是最小值，不是最大值！

陷阱2：認為 heap 是完全排序的
  [1, 2, 9, 5] 是有效的 heap
  但不完全排序（5 和 9 的位置沒關係）

陷阱3：直接修改堆的元素
  h = [1, 2, 3]
  h[0] = 999  # ✗ 破壞了堆的性質！
  
  正確做法：
  heapq.heapreplace(h, 999)  # ✓ 維持堆性質

陷阱4：堆上的元素必須可比較
  h = [1, "a", 2]  # ✗ TypeError
  heapq.heapify(h)  # 無法比較 int 和 str

解決方案：使用元組
  h = [(1, "task1"), (2, "task2")]
  heapq.heapify(h)  # ✓ 按第一個元素比較
  
最佳實踐：

✓ 推薦做法
  import heapq
  
  # 找 top-n
  nums = [5, 1, 9, 2, ...]
  
  # 方法1：nsmallest（最簡單）
  smallest = heapq.nsmallest(10, nums)
  
  # 方法2：手動堆化（如需多次 pop）
  h = nums[:]
  heapq.heapify(h)
  smallest = [heapq.heappop(h) for _ in range(10)]

✗ 避免做法
  # 對所有數據排序後取前 n 個
  sorted_nums = sorted(nums)  # ✗ 浪費時間
  top_n = sorted_nums[:n]
  
✗ 容易出錯
  # 修改堆中的元素後不重新平衡
  h = [1, 2, 3]
  h[0] = 999  # ✗ 堆性質被破壞

性能總結：

操作          | 堆        | 排序列表  | 未排序列表
查詢最小值    | O(1)      | O(1)      | O(n)
添加元素      | O(log n)  | O(n)      | O(1)
移除最小值    | O(log n)  | O(1)      | O(n)
Top-N         | O(n+k log n) | O(n log n) | O(n*k)

推薦場景：
- 實時找最小/最大的 N 個元素 ✓
- 優先級隊列 ✓
- 圖算法（Dijkstra、Prim）✓
"""
