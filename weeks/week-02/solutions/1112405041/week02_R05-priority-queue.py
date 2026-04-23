# 【Bloom 階段：R - 記憶與基本操作】
# R5. 實作一個簡單的優先權隊列 (PriorityQueue)
# August 的惡意提醒：在 Week 03 的模擬題中，如果有多個機器人依權重排序執行，
# 這個類別就是你的底層引擎。注意 index 的使用是為了避免「同優先權對象」的比較報錯。

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """
        August 教學點：
        1. 使用 -priority 是為了將預設的最小堆 (min-heap) 模擬成最大堆。
        2. 加入 self._index 是為了確保在 priority 相同時，能根據「進入順序」排序，
           同時也防止 item 物件本身不支持比較運算而報錯。
        """
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """取出最高優先權的對象"""
        return heapq.heappop(self._queue)[-1]

# 測試
pq = PriorityQueue()
pq.push("Task Low", 1)
pq.push("Task High", 5)
pq.push("Task Mid", 3)

print(f"Popped: {pq.pop()}") # 應該是 Task High
