"""
主題名：R05 - 優先隊列（Priority Queue）
學習目標：掌握如何使用 heapq 實現優先隊列，理解其在任務調度中的應用。

核心概念：
  1. 優先隊列是一種特殊的隊列，元素按優先級排序
  2. 使用 heapq 可以高效地實現優先隊列
  3. 使用計數器確保相同優先級的元素保持插入順序
  4. 取反優先級實現最大優先隊列（heapq 默認是最小堆）
  5. 適用於任務調度、事件處理、Dijkstra 算法等場景
"""

import heapq


class PriorityQueue:
    """
    優先隊列實現
    
    特點：
      - 高優先級的元素先出隊
      - 相同優先級按插入順序處理（FIFO）
      - O(log n) 的插入和移除複雜度
    """
    
    def __init__(self):
        """初始化優先隊列"""
        self._queue = []      # 存儲 (優先級, 順序計數, 元素) 的元組
        self._index = 0       # 計數器，用於記錄插入順序
    
    def push(self, item, priority):
        """
        向隊列中添加元素
        
        參數：
          item: 要添加的元素
          priority: 優先級（數字越小優先級越高）
        """
        # 使用負優先級是為了實現降序（高優先級先處理）
        # _index 確保相同優先級的元素按插入順序處理
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        """
        移除並返回優先級最高的元素
        
        返回：
          優先級最高的元素
        """
        return heapq.heappop(self._queue)[-1]  # 返回最後一個元素（item）
    
    def is_empty(self):
        """檢查隊列是否為空"""
        return len(self._queue) == 0
    
    def size(self):
        """返回隊列中元素個數"""
        return len(self._queue)
    
    def peek(self):
        """查看優先級最高的元素而不移除"""
        if self.is_empty():
            return None
        return self._queue[0][-1]
    
    def __str__(self):
        """打印隊列內容"""
        return f"PriorityQueue({len(self._queue)} items)"


def example_basic_priority_queue():
    """
    示例 1：基本優先隊列操作
    
    說明：
      - 演示優先隊列的基本操作：push 和 pop
      - 優先級數字越小，優先級越高
      - 相同優先級按插入順序處理
    """
    print("=== 基本優先隊列操作 ===\n")
    
    pq = PriorityQueue()
    
    # 添加任務，優先級不同
    tasks = [
        ("完成報告", 3),
        ("回覆郵件", 2),
        ("修復 Bug", 1),      # 優先級最高
        ("代碼審查", 2),      # 與回覆郵件相同優先級
        ("計劃會議", 4),
    ]
    
    print("添加任務（優先級越低越重要）:")
    for task, priority in tasks:
        pq.push(task, priority)
        print(f"  [{priority}] {task}")
    
    print(f"\n隊列狀態: {pq}\n")
    
    print("按優先級順序處理任務:")
    while not pq.is_empty():
        task = pq.pop()
        print(f"  ✓ 處理: {task}")


def example_same_priority_fifo():
    """
    示例 2：相同優先級的 FIFO 順序
    
    說明：
      - 優先隊列使用計數器確保相同優先級的元素保持插入順序
      - 這對於公平性很重要
    """
    print("\n" + "="*60)
    print("=== 相同優先級的 FIFO 順序 ===\n")
    
    pq = PriorityQueue()
    
    # 添加相同優先級的多個任務
    print("添加相同優先級的任務:")
    for i in range(1, 5):
        task = f"任務 {i}"
        pq.push(task, priority=1)
        print(f"  push: {task}")
    
    print("\n快速出隊順序（保持插入順序）:")
    while not pq.is_empty():
        task = pq.pop()
        print(f"  pop: {task}")


def example_tasks_scheduling():
    """
    示例 3：任務調度系統
    
    說明：
      - 實際應用：操作系統任務調度
      - 系統任務優先級最高，然後是用戶重要任務，最後是後台任務
    """
    print("\n" + "="*60)
    print("=== 任務調度系統 ===\n")
    
    pq = PriorityQueue()
    
    # 優先級定義：1=系統 2=高 3=中 4=低 5=後台
    print("優先級 1=系統 | 2=高 | 3=中 | 4=低 | 5=後台\n")
    
    # 模擬系統中發生的各種任務
    scheduler_tasks = [
        ("清理緩存", 5),          # 後台任務
        ("定期備份", 4),          # 低優先級
        ("用戶登入檢查", 2),      # 高優先級
        ("系統更新", 1),          # 最高優先級
        ("生成日誌", 4),          # 低優先級
        ("數據同步", 3),          # 中優先級
        ("處理緊急告警", 1),      # 最高優先級
    ]
    
    print("任務入隊:")
    for task, priority in scheduler_tasks:
        pq.push(task, priority)
        print(f"  [{priority}] {task}")
    
    print(f"\n隊列中有 {pq.size()} 個任務待執行\n")
    
    print("按優先級執行:")
    order = 1
    while not pq.is_empty():
        task = pq.pop()
        print(f"  {order}. {task}")
        order += 1


def example_patient_triage():
    """
    示例 4：醫院掛號系統（患者分類）
    
    說明：
      - 優先隊列的實際應用：患者優先級分類
      - 緊急患者優先看診
    """
    print("\n" + "="*60)
    print("=== 醫院患者分類系統 ===\n")
    
    # 優先級：1=緊急 2=重要 3=普通 4=一般問詢
    triage_queue = PriorityQueue()
    
    # 患者信息：(患者ID, 姓名, 症狀, 優先級)
    patients = [
        (101, "李先生", "普通感冒", 3),
        (102, "王女士", "急性心肌梗塞", 1),       # 最緊急
        (103, "張小姐", "骨折", 2),               # 重要
        (104, "劉先生", "頭暈", 3),
        (105, "陳老先生", "休克", 1),             # 最緊急
        (106, "吳女士", "咨詢費用", 4),           # 一般問詢
    ]
    
    print("患者到達（掛號順序）:")
    for patient_id, name, symptom, priority in patients:
        triage_queue.push((patient_id, name, symptom), priority)
        priority_names = {1: "緊急", 2: "重要", 3: "普通", 4: "一般"}
        print(f"  [#{patient_id}] {name:4} - {symptom:10} [{priority_names[priority]}]")
    
    print(f"\n看診順序（按優先級）:")
    order = 1
    while not triage_queue.is_empty():
        patient_id, name, symptom = triage_queue.pop()
        print(f"  {order}. 請 #{patient_id} {name:4} 進診室 ({symptom})")
        order += 1


def example_event_processing():
    """
    示例 5：事件處理系統
    
    說明：
      - 優先隊列也用於事件驅動系統
      - 不同類型的事件有不同的優先級
    """
    print("\n" + "="*60)
    print("=== 事件處理系統 ===\n")
    
    event_queue = PriorityQueue()
    
    # 事件：(事件類型, 時間戳, 描述) - 優先級
    events = [
        ("USER_CLICK", "2024-01-01 10:05:00", "用戶點擊按鈕", 4),
        ("DATABASE_ERROR", "2024-01-01 10:04:30", "數據庫連接失敗", 1),
        ("API_RESPONSE", "2024-01-01 10:05:05", "API 響應超時", 2),
        ("MEMORY_WARNING", "2024-01-01 10:04:45", "內存使用率 90%", 2),
        ("USER_LOGIN", "2024-01-01 10:03:00", "新用戶登入", 3),
    ]
    
    print("事件發生順序（時間順序）:")
    for event_type, timestamp, desc, priority in events:
        event_queue.push((event_type, timestamp, desc), priority)
        priority_names = {1: "CRITICAL", 2: "ERROR", 3: "WARNING", 4: "INFO"}
        print(f"  [{priority_names[priority]:8}] {timestamp} - {event_type}: {desc}")
    
    print(f"\n事件處理順序（按優先級，而非時間）:")
    priority_names = {1: "CRITICAL", 2: "ERROR", 3: "WARNING", 4: "INFO"}
    while not event_queue.is_empty():
        event_type, timestamp, desc = event_queue.pop()
        print(f"  經理處理: [{event_type:15}] {desc}")


def example_dijkstra_algorithm():
    """
    示例 6：Dijkstra 最短路徑算法
    
    說明：
      - 優先隊列在圖算法中的應用
      - Dijkstra 算法使用優先隊列快速獲取最小距離的節點
    """
    print("\n" + "="*60)
    print("=== Dijkstra 算法應用 ===\n")
    
    print("圖的結構:")
    print("    A --1-- B")
    print("    |       |")
    print("    4       2")
    print("    |       |")
    print("    C --3-- D")
    print()
    
    # 簡化的 Dijkstra 演示
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2},
        'C': {'A': 4, 'D': 3},
        'D': {'B': 2, 'C': 3},
    }
    
    def dijkstra(start):
        """簡化的 Dijkstra 算法演示"""
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        pq = PriorityQueue()
        pq.push(start, 0)
        
        visited = set()
        
        while not pq.is_empty():
            current = pq.pop()
            if current in visited:
                continue
            
            visited.add(current)
            print(f"訪問節點 {current} (距離: {distances[current]})")
            
            for neighbor, distance in graph[current].items():
                new_dist = distances[current] + distance
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    pq.push(neighbor, new_dist)
        
        return distances
    
    print("從 A 出發的最短距離:")
    result = dijkstra('A')
    for node, dist in result.items():
        print(f"  到達 {node}: {dist}")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python 優先隊列教學程式\n")
    print("="*60)
    
    example_basic_priority_queue()
    example_same_priority_fifo()
    example_tasks_scheduling()
    example_patient_triage()
    example_event_processing()
    example_dijkstra_algorithm()
    
    print("\n" + "="*60)
    print("總結：")
    print("  • 優先隊列按優先級而非插入順序排隊")
    print("  • 使用 heapq 實現，O(log n) 複雜度")
    print("  • 計數器確保相同優先級的 FIFO 順序")
    print("  • 應用：任務調度、患者分類、事件處理、最短路徑等")
    print("  • 負優先級可實現最大優先隊列")
    print("="*60)
