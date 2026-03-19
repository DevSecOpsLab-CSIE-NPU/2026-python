"""
U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）

功能：展示 deque 的自動旋轉機制

核心概念：
  - deque：雙端隊列（double-ended queue）
  - maxlen：設定隊列的最大容量
  - 自動淘汰：超過容量時自動刪除舊元素
  - 固定大小：容量固定不變

關鍵特徵：
  1. 創建時指定 maxlen（必須在創建時設定）
  2. 當達到最大容量後，新增元素：
     - 自動移除最舊的元素（在另一端）
     - 新元素從另一端加入
  3. 保留最近的 N 條記錄 ✓
  4. 完美用於「滑動窗口」場景

應用場景：
  - 保留最近的 N 條日誌
  - 保留最近的 N 次操作（用於撤銷功能）
  - 性能監控（最近 N 次的平均值）
  - 固定大小的緩衝區
"""

from collections import deque
"""
導入 deque 模塊

說明：
  - collections：Python 標準庫中的容器模組
  - deque：優化的雙端隊列，支持 O(1) 的兩端操作
  - vs list：list 在頭部刪除是 O(n)，deque 是 O(1)
"""

q = deque(maxlen=3)
"""
創建一個容量有限的 deque

參數分析：
  - maxlen=3：設定最大容量為 3
  - 一旦容量滿，新增元素時會自動移除舊元素

初始狀態：
  q = deque([], maxlen=3)
  → 空的隊列，最多可容納 3 個元素

重要特性：
  - maxlen 是創建時必須指定的（不能後改）
  - 一旦設定就不可更改
  - 如果不指定 maxlen，deque 就是無限大小

vs 普通隊列：
  普通 queue：q = queue.Queue(maxsize=3)
    - 達到容量時，put() 會阻塞
    - 用於線程同步
  
  deque with maxlen：q = deque(maxlen=3)
    - 達到容量時自動丟棄舊元素
    - 簡單高效，無阻塞
"""

for i in [1, 2, 3, 4, 5]:
    q.append(i)
    """
    逐個添加元素 1, 2, 3, 4, 5
    
    理解 maxlen 的自動淘汰機制：
    
    迭代 1：append(1)
      操作前：q = []
      操作後：q = [1]
      容量用途：1/3
    
    迭代 2：append(2)
      操作前：q = [1]
      操作後：q = [1, 2]
      容量用途：2/3
    
    迭代 3：append(3)
      操作前：q = [1, 2]
      操作後：q = [1, 2, 3]
      容量用途：3/3 ✓ 已滿
    
    迭代 4：append(4)【關鍵時刻】
      操作前：q = [1, 2, 3]（已滿）
      自動淘汰機制啟動：
        - 因為容量已滿（3 個元素）
        - 新元素 4 要被加入
        - 自動移除最舊的元素 1（左端）
      操作後：q = [2, 3, 4]
      
      說明：
        - deque 從「左端」（oldest）移除元素
        - 新元素從「右端」（newest）加入
        - 就像旋轉一樣
    
    迭代 5：append(5)
      操作前：q = [2, 3, 4]（已滿）
      自動淘汰機制啟動：
        - 移除最舊元素 2
        - 加入新元素 5
      操作後：q = [3, 4, 5]
    
    最終結果：q = [3, 4, 5]
    
    重要觀察：
      - 結果恰好是最後 3 個元素 ✓
      - 前面的 1, 2 被自動丟棄了
      - 順序保持不變（FIFO 特性）
    """
    pass  # 這裡只用於演示，省略了 print


# 結果只剩 [3, 4, 5]
"""
最終狀態說明

結果分析：
  q = deque([3, 4, 5], maxlen=3)
  
  包含的元素：
    - 3（第 3 個加入的）
    - 4（第 4 個加入的）
    - 5（第 5 個加入的）
  
  丟棄的元素：
    - 1（第 1 個加入的）✗
    - 2（第 2 個加入的）✗
  
  為什麼丟棄？
    - 容量限制為 3
    - 保留最新的 3 個元素
    - 舊的被淘汰

核心理解：

maxlen 的工作方式
  ┌─────────────────────────────┐
  │ append() 新元素來自右端      │
  │     ↓                       │
  │  [3, 4, 5]                  │
  │     ↑                       │
  │ 舊元素從左端自動移除         │
  └─────────────────────────────┘
  
  這種機制導致「滑動窗口」效應
  → 始終保留最新的 N 個元素

性能特性：

時間複雜度：
  - append()：O(1)
  - popleft()：O(1)
  - appendleft()：O(1)
  - pop()：O(1)
  
  vs list（不使用 maxlen）：
  - append()：O(1)
  - popleft()：O(n) ✗ 很慢！
  - pop()：O(1)

空間複雜度：
  - O(maxlen)：固定大小
  - 內存占用可預測
  - 永遠不會超過 maxlen

常見用途詳解：

用途1：保留最近 N 條日誌
  logs = deque(maxlen=100)
  
  for event in events:
      logs.append(event)
  
  最後 100 條自動保留 ✓

用途2：計算滑動窗口的平均值
  from collections import deque
  
  window = deque([1, 2, 3], maxlen=3)
  
  def add_and_compute_avg(value):
      window.append(value)  # 舊值自動移除
      return sum(window) / len(window)
  
  add_and_compute_avg(4)  # [2, 3, 4] 的平均值 = 3.0
  add_and_compute_avg(5)  # [3, 4, 5] 的平均值 = 4.0

用途3：實現撤銷功能
  undo_stack = deque(maxlen=10)  # 最多保留 10 次操作
  
  def do_action(action):
      # 執行操作...
      undo_stack.append(action)  # 記錄操作
  
  def undo():
      if undo_stack:
          action = undo_stack.pop()  # 從右端取出最近的操作
          # 撤銷操作...

用途4：性能監控
  performance = deque(maxlen=60)  # 保留最近 60 秒
  
  for second in range(1000):
      response_time = measure_response_time()
      performance.append(response_time)
      
      avg = sum(performance) / len(performance)
      print(f"最近 60 秒平均響應時間：{avg:.2f}ms")

方向參數：

append() 和 popleft() 的方向：
  q = deque([1, 2, 3], maxlen=3)
  
  q.append(4)
  → [2, 3, 4]（新元素從右端進，舊元素從左端出）
  
  q.appendleft(0)
  → [0, 3, 4]（新元素從左端進，舊元素從右端出）

這說明 deque 是「雙端」的：
  - 可以從兩端添加
  - 也可以從兩端移除
  - maxlen 時自動從「另一端」移除元素

邊界情況：

情況1：maxlen = 0
  q = deque(maxlen=0)
  q.append(1)
  → q = deque([], maxlen=0)
  → 所有元素都被立即丟棄
  → 基本無用，但可能用於性能測試

情況2：maxlen 比初始元素少
  q = deque([1, 2, 3, 4, 5], maxlen=3)
  → 只保留最後 3 個：[3, 4, 5]
  → 前面的自動丟棄

情況3：maxlen 比初始元素多
  q = deque([1, 2, 3], maxlen=10)
  → 保持 [1, 2, 3]
  → 容量有 7 個空位
  → 正常工作

常見錯誤與解決：

錯誤1：試圖更改 maxlen
  q = deque(maxlen=3)
  q.maxlen = 5  # AttributeError：maxlen 是只讀的
  
  解決方案：
  # 如需更改，需要創建新的 deque
  new_q = deque(q, maxlen=5)

錯誤2：期望 maxlen 為負數
  q = deque(maxlen=-1)  # ValueError！
  
  規則：
  - maxlen 必須 ≥ 0
  - maxlen = 0：所有元素都被丟棄
  - maxlen = None：無限大小（默認）

錯誤3：混淆 deque 與普通 list
  d = deque([1, 2, 3], maxlen=3)
  l = [1, 2, 3]
  
  d.append(4)  # [2, 3, 4]（自動丟棄）
  l.append(4)  # [1, 2, 3, 4]（擴展）✗
  
  比較結果不同！

vs 其他實現方式：

方案1：deque with maxlen（推薦）✓
  from collections import deque
  recent = deque(maxlen=10)
  
  優點：
    - 簡潔、高效、O(1)
    - 自動管理容量
    - 無需手動移除舊元素
  
  缺點：
    - maxlen 創建後無法更改
    - 無法指定移除策略

方案2：手動管理 list
  recent = []
  
  # 新增元素
  recent.append(new_item)
  
  # 手動移除舊元素
  if len(recent) > 10:
      recent.pop(0)  # ✗ O(n) 很慢！
  
  缺點：
    - 手動操作容易出錯
    - 性能差（O(n)）

方案3：使用 collections.OrderedDict
  from collections import OrderedDict
  
  recent = OrderedDict()
  recent[key] = value
  
  if len(recent) > 10:
      recent.popitem(last=False)
  
  缺點：
    - 複雜度更高
    - 需要手動限制大小

推薦：使用 deque 搭配 maxlen ✓

最佳實踐：

✓ 推薦做法
  from collections import deque
  
  # 明確指定容量
  logs = deque(maxlen=1000)
  
  # 直接 append，不用擔心內存
  for log in log_stream:
      logs.append(log)
  
  # 轉換為列表使用
  recent_logs = list(logs)

✗ 避免做法
  # 每次都手動檢查並移除
  logs = []
  
  for log in log_stream:
      logs.append(log)
      if len(logs) > 1000:  # ✗ 低效
          logs.pop(0)

✗ 容易忘記
  # 創建後試圖更改 maxlen
  q = deque([1, 2, 3], maxlen=3)
  # ... 後來想改為 5
  # ✗ 不支持，需要重新創建

相關概念預告：
  - 1.4：defaultdict 自動創建默認值
  - 1.5：OrderedDict 保持插入順序
  - 2.1：隊列與棧的性能對比
"""
