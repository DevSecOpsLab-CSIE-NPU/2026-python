"""
U05: priority queue 為什麼要加 index

當 priority 相同時，heapq 會繼續比較後面的值。
若後面的物件不能直接比較，就會出錯。
"""

import heapq


class Item:
    def __init__(self, name):
        self.name = name


pq = []

# 如果直接放 (priority, item)，當 priority 相同時，
# heapq 會試著比較 Item 物件，這裡會產生 TypeError。
# heapq.heappush(pq, (-1, Item("a")))
# heapq.heappush(pq, (-1, Item("b")))

# 加入遞增的 index 後，就能在 priority 相同時穩定排序。
idx = 0
heapq.heappush(pq, (-1, idx, Item("a")))
idx += 1
heapq.heappush(pq, (-1, idx, Item("b")))
idx += 1
