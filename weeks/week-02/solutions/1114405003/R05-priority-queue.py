"""
R05：自製 PriorityQueue

學習目標：
1. 用 heapq 實作簡易優先佇列。
2. priority 越大越先出列（透過負號轉換）。
3. 同 priority 時，用 index 保持先進先出（穩定排序）。
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # heapq 是最小堆，所以用負號把「大優先級」轉成「小數值」。
        heapq.heappush(self._queue, (-priority, self._index, item))
        print(f"  push -> item={item}, priority={priority}, heap_entry={(-priority, self._index, item)}")
        self._index += 1

    def pop(self):
        popped = heapq.heappop(self._queue)
        print("  pop  -> heap_entry=", popped)
        return popped[-1]


class Task:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Task({self.name!r})"


def main():
    print("=== R05 PriorityQueue ===")
    q = PriorityQueue()
    q.push(Task("寫作業"), priority=2)
    q.push(Task("繳報告"), priority=5)
    q.push(Task("整理筆記"), priority=2)

    print("[出列1]", q.pop())
    print("[出列2]", q.pop())
    print("[出列3]", q.pop())


if __name__ == "__main__":
    main()
