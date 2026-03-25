# ============================================================================
# R5. 優先級隊列 (Priority Queue)（1.5）
# ============================================================================
# 本題展示如何用 heapq 實現一個完整的優先級隊列類。
# 核心：使用 (優先級, index, 項目) 三元組避免比較項目本身。
# ============================================================================

import heapq

print("【優先級隊列基本概念】")
print("=" * 50)
print()

print("優先級隊列的特點：")
print("  - 總是返回優先級最高（最小）的元素")
print("  - 支援動態新增元素")
print("  - 時間複雜度：O(log n)\n")

class PriorityQueue:
    """簡單的優先級隊列實現"""
    
    def __init__(self):
        """初始化隊列"""
        self._queue = []      # 存儲堆
        self._index = 0       # 追蹤插入順序
    
    def push(self, item, priority):
        """將元素加入隊列
        
        參數：
            item: 要加入的元素
            priority: 優先級（越小越優先）
        """
        # 使用 (優先級, index, 項目) 的三元組
        # index 確保了當優先級相同時，按插入順序處理
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        """移除並返回優先級最高的元素"""
        return heapq.heappop(self._queue)[-1]


print("【使用示例】")
print("=" * 50)
print()

print("建立優先級隊列")
pq = PriorityQueue()
print()

print("添加任務（優先級越高，數字越大）：")
tasks = [
    ('寫報告', 3),
    ('修復 bug', 5),
    ('喝咖啡', 1),
    ('開會', 4),
]

for task, priority in tasks:
    pq.push(task, priority)
    print(f"  優先級 {priority}: {task}")
print()

print("按優先級順序處理任務：")
while True:
    try:
        task = pq.pop()
        print(f"  執行：{task}")
    except IndexError:
        break
print()

print("=" * 50)
print("【設計解析 - 為什麼使用 (-priority, index, item)？】")
print("=" * 50)
print()

print("❌ 問題：為什麼不直接用 (priority, item)？\n")
print("原因：")
print("  1. heapq 是最小堆「  優先級小 = 優先取出")
print("  2. 如果優先級相同，heapq 會比較第二個元素")
print("  3. 如果第二個元素是不可比較的物件，會報 TypeError\n")

print("例如：")
print("  heappush(q, (5, 'task1'))")
print("  heappush(q, (5, 'task2'))")
print("  # 相同優先級時，heapq 會試圖比較字符串 'task1' 和 'task2'")
print("  # 沒問題（字符串可比）")
print()
print("但如果項目是物件：")
print("  heappush(q, (5, Task('重要')))")
print("  heappush(q, (5, Task('緊急')))")
print("  # TypeError: < not supported between Task instances!\n")

print("✓ 解決方案：使用 index 作為 tiebreaker\n")
print("優勢：")
print("  1. index 是整數，總是可比較")
print("  2. 不同優先級時，index 不會被比較")
print("  3. 相同優先級時，按插入順序（FIFO）處理")
print("  4. 完美避免了比較項目本身的問題\n")

print("=" * 50)
print("【完整實現 + 演示】")
print("=" * 50)
print()

class Task:
    """示例：任務類"""
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    def __repr__(self):
        return f"Task({self.name}, P{self.priority})"

pq2 = PriorityQueue()
print("添加具有相同優先級的任務：")
pq2.push(Task('A', 5), 5)
pq2.push(Task('B', 5), 5)
pq2.push(Task('C', 5), 5)
print(f"  Task A, Priority 5")
print(f"  Task B, Priority 5")
print(f"  Task C, Priority 5\n")

print("處理（按 FIFO 順序，因為優先級相同）：")
for i in range(3):
    task = pq2.pop()
    print(f"  {i+1}. {task}")
print()

print("=" * 50)
print("【最佳實踐】")
print("=" * 50)
print("""
✓ 使用 3-元組 (優先級, index, item)
✓ 使用裝飾器模式（decorator pattern）
✓ 考慮使用 queue.PriorityQueue（線程安全）
✓ 文件系統的優先級隊列
✓ 作業調度系統
✓ Dijkstra 最短路徑算法
""")
