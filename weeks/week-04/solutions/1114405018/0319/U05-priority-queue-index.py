"""
U5. 優先佇列為何要加 index（1.5）

功能：展示在優先隊列中使用自定義對象時的常見陷阱

核心問題：
  - heapq 中，元組按第一個優先級排序
  - 當優先級相同時，heapq 繼續比較下一個元素
  - 自定義的 Item 對象沒有定義 < 運算符 → TypeError ✗

解決方案：
  - 在優先級和對象之間插入 index
  - index 用於作為「打破平手」的標準
  - 避免直接比較 Item 對象 ✓

好處：
  - 確保對象不會互相比較
  - index 拋出平手時自動按插入順序排序
  - 代碼簡潔且高效
"""

import heapq
"""
heapq 模塊：最小堆實現

說明：
  - heapq 是 Python 的優先隊列實現
  - 基於二進制堆演算法
  - 支持 O(log n) 的插入和移除操作
  - 對於最小堆：最小元素總是在索引 0
"""

class Item:
    """自定義的項目類別，代表優先隊列中的元素"""
    def __init__(self, name):
        self.name = name
        """
        初始化項目
        
        參數：
          - name: 項目的名稱（如 'a', 'b' 等）
        """

pq = []
"""
初始化一個空的優先隊列

說明：
  - pq 是存儲堆元素的列表
  - heapq 運作在 list 上，不需要專門的 Queue 類
  - 堆會自動維持堆性質（parent ≤ children）
"""

# 若只放 (priority, item)，同 priority 會比較 item，Item 不支援 < 會炸
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError
"""
問題演示：為什麼這個代碼會失敗？

嘗試的代碼：
  heapq.heappush(pq, (-1, Item('a')))
  heapq.heappush(pq, (-1, Item('b')))

元組結構：(priority, item)
  - priority = -1（兩個都相同）
  - item = Item('a') 或 Item('b')

執行過程分析：

步驟 1：推入第一個元素
  heapq.heappush(pq, (-1, Item('a')))
  → pq = [(-1, Item('a'))]
  → 堆中只有一個元素，無需比較
  → 成功 ✓

步驟 2：推入第二個元素
  heapq.heappush(pq, (-1, Item('b')))
  
  堆操作步驟：
    1. 將新元素添加到末尾
       pq = [(-1, Item('a')), (-1, Item('b'))]
    
    2. 執行「上浮」操作（sift up）
       比較新元素與其父節點：
       (-1, Item('b')) vs (-1, Item('a'))
    
    3. 優先級相同（都是 -1）
       → heapq 需要比較元組的下一個元素
       → 嘗試執行：Item('b') < Item('a')
    
    4. Item 類沒有定義 __lt__ (< 運算符)
       → Python 拋出 TypeError ✗

錯誤信息：
  TypeError: '<' not supported between instances of 'Item' and 'Item'

為什麼會是這個錯誤？

元組比較規則：
  (a, b) vs (c, d)
  
  1. 先比較第一個元素 a vs c
  2. 如果 a == c，再比較 b vs d
  3. 如果需要比較 b vs d 卻不支持 < → TypeError

在我們的例子中：
  (-1, Item('a')) vs (-1, Item('b'))
  
  1. 比較 -1 vs -1（相等）
  2. 需要比較 Item('a') vs Item('b')（失敗！）

問題的三層次：

層次1：優先級相同
  priority_a = priority_b
  → 需要使用次級排序標準

層次2：對象無法比較
  Item 類沒實現 __lt__
  → 不能使用對象作為次級排序

層次3：設計不當
  直接將對象放入堆
  → 當優先級相同時會出問題

解決方案1（不推薦）：為 Item 類添加 __lt__
  class Item:
      def __init__(self, name):
          self.name = name
      
      def __lt__(self, other):
          return self.name < other.name
  
  現在可以比較 Item 了
  
  缺點：
    ✗ 語義上不對（Item 本不應該有優先級概念）
    ✗ 如果 name 相同，仍需要額外的 tiebreaker
    ✗ 違反單一責任原則

解決方案2（推薦）✓：使用 index 作為 tiebreaker
  idx = 0
  heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
  heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1
  
  優點：
    ✓ 不需要修改 Item 類
    ✓ 當優先級相同時自動按插入順序排序
    ✓ 語義清楚：優先級 → 插入順序 → 對象
    ✓ 簡單有效 ✓✓✓
"""

# 正解：加 index 避免比較 item
idx = 0
"""
初始化索引計數器

說明：
  - idx 迹傳索引編號
  - 每次插入新元素時遞增
  - 用於在優先級相同時決定順序
  
用途：
  - 作為優先隊列元組的第二個元素
  - 保證不同的元素有不同的 index
  - index 是整數，總可以比較
"""

heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
"""
推入第一個元素

元組結構：(-1, 0, Item('a'))
  - priority = -1（優先級）
  - index = 0（插入順序）
  - item = Item('a')（實際的對象）

執行過程：
  1. 構建元組 (-1, 0, Item('a'))
  2. 推入堆
  3. idx 遞增，現在 idx = 1

堆狀態：
  pq = [(-1, 0, Item('a'))]

說明：
  - 堆中只有一個元素，無需比較
  - 成功插入 ✓
"""

heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1
"""
推入第二個元素

元組結構：(-1, 1, Item('b'))
  - priority = -1（與第一個相同）
  - index = 1（不同的插入順序）
  - item = Item('b')

執行過程：

步驟 1：添加到末尾
  pq = [(-1, 0, Item('a')), (-1, 1, Item('b'))]

步驟 2：執行上浮操作
  比較 (-1, 1, Item('b')) vs (-1, 0, Item('a'))
  
  1. 比較優先級：-1 vs -1（相等）
  2. 比較 index：1 vs 0（1 > 0，所以不需要上浮）
  3. 完成 ✓

堆狀態：
  pq = [(-1, 0, Item('a')), (-1, 1, Item('b'))]

關鍵點：
  - 優先級相同時，比較 index
  - index 是整數，總是可比較的
  - 無需比較 Item 對象 ✓
  - Item('b') 從未被比較

idx 更新：
  idx 從 1 遞增到 2
  用於下一個插入

為什麼 index 解決問題？

元組比較鏈：
  (-1, idx1, Item) vs (-1, idx2, Item)
  
  1. 比較 -1 vs -1 → 相等，繼續
  2. 比較 idx1 vs idx2 → 必定不等（不同的插入順序）
  3. 決定順序，無需比較 Item ✓

index 的角色：
  - 作為「tiebreaker」（打破平手）
  - 確保比較在 index 層就停止
  - Item 對象永遠不會被比較

具體例子演示：

假設我們繼續添加：
  heapq.heappush(pq, (-2, idx, Item('c'))); idx += 1
  heapq.heappush(pq, (-1, idx, Item('d'))); idx += 1

堆中元素：
  [(-1, 0, Item('a')), (-1, 1, Item('b')), (-2, 2, Item('c')), (-1, 3, Item('d'))]

彈出順序（heappop）：
  1. pop()→ (-1, 0, Item('a'))（優先級 -1，最早插入）
  2. pop()→ (-1, 1, Item('b'))（優先級 -1，第二插入）
  3. pop()→ (-1, 3, Item('d'))（優先級 -1，第四插入）
  4. pop()→ (-2, 2, Item('c'))（優先級 -2，最低）

觀察：
  - 優先級 -1 的項按插入順序彈出
  - 優先級 -2 的項最後彈出
  - 無需比較 Item 對象 ✓

常見錯誤：

錯誤1：優先級相同時忘記 index
  heapq.heappush(pq, (priority, item))  # ✗
  → 如果優先級相同會 TypeError

錯誤2：index 不遞增
  heapq.heappush(pq, (priority, 0, item))  # ✗
  heapq.heappush(pq, (priority, 0, item))  # 兩個都是 0
  → 無法正確區分

錯誤3：顛倒 priority 和 index 的順序
  heapq.heappush(pq, (idx, priority, item))  # ✗
  → 先按 idx 排序，再按 priority，邏輯錯誤

通用模式（最佳實踐）：

推薦的優先隊列模式：
  import heapq
  
  class PriorityQueue:
      def __init__(self):
          self.pq = []
          self.entry_count = 0
      
      def push(self, priority, item):
          # 優先級用負號表示最大堆
          heapq.heappush(
              self.pq,
              (priority, self.entry_count, item)
          )
          self.entry_count += 1
      
      def pop(self):
          priority, count, item = heapq.heappop(self.pq)
          return item
  
  # 使用
  pq = PriorityQueue()
  pq.push(-1, Item('a'))
  pq.push(-1, Item('b'))
  pq.push(-2, Item('c'))
  
  while pq.pq:
      item = pq.pop()
      print(item.name)

性能分析：

時間複雜度：
  - push（帶 index）：O(log n)
  - pop：O(log n)
  - 比較操作：O(1)（因為在 index 層停止）

空間複雜度：
  - O(n)：n 為隊列元素數

vs 其他方案：

方案1：使用 heapq 加 index（當前方案）✓
  優點：
    - 簡單、高效
    - 無需修改 Item 類
    - 代碼清晰
  缺點：
    - 需要手動管理 idx 計數器

方案2：為 Item 類實現 __lt__
  優點：
    - 不需要額外的 index
  缺點：
    - 語義不清
    - Item 類變得複雜
    - 實現的比較邏輯可能有問題

方案3：使用 PriorityQueue.PriorityQueue（隊列模塊）
  from queue import PriorityQueue
  
  pq = PriorityQueue()
  pq.put((priority, item))  # 同樣的問題！
  
  需要同樣的解決方案

相關主題預告：

- 1.6：使用 heapq.nlargest/nsmallest
- 2.1：堆的實現細節
- 2.2：優先隊列的高級用途（如 Dijkstra 演算法）

除錯技巧：

技巧1：檢查隊列內容
  import heapq
  
  pq = [(-1, 0, Item('a')), (-1, 1, Item('b'))]
  print(pq)  # 查看堆的實際結構

技巧2：手動驗證堆性質
  def is_valid_heap(arr):
      for i in range(len(arr)):
          left = 2*i + 1
          right = 2*i + 2
          if left < len(arr) and arr[i] > arr[left]:
              return False
          if right < len(arr) and arr[i] > arr[right]:
              return False
      return True

技巧3：逐個 pop 觀察順序
  while pq:
      priority, idx, item = heapq.heappop(pq)
      print(f"Pop: priority={priority}, idx={idx}, item={item.name}")

結論：

✓ 正確的做法
  使用 (priority, index, item) 的三元組
  → 避免比較 Item 對象
  → 優先級相同時按插入順序排序
  → 簡潔有效

核心要點：
  1. heapq 比較元組的所有元素
  2. 優先級相同時需要 tiebreaker
  3. index 是完美的 tiebreaker（整數，無限制）
  4. 無需修改 Item 類或實現 __lt__
"""
