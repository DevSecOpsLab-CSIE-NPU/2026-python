# U05 優先佇列需要 tie-breaker
# 重點：priority 相同時，heap 會比較後續欄位；若物件不可比較會 TypeError。

import heapq


class Item:
    def __init__(self, name):
        self.name = name


pq = []

# 下列寫法在 priority 相同時會嘗試比較 Item 物件本身，造成 TypeError。
# heapq.heappush(pq, (-1, Item("a")))
# heapq.heappush(pq, (-1, Item("b")))

# 解法：加入遞增 index 作為第二排序鍵，確保可比較且維持穩定順序。
idx = 0
heapq.heappush(pq, (-1, idx, Item("a")))
idx += 1
heapq.heappush(pq, (-1, idx, Item("b")))
idx += 1
