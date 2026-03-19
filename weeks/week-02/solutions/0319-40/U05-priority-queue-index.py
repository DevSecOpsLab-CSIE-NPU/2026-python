# U5. 優先佇列為何要加 index（1.5）

import heapq


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item({self.name!r})"


pq = []

# 正解：加 index 避免比較 item
idx = 0
heapq.heappush(pq, (-1, idx, Item('a')))
idx += 1
heapq.heappush(pq, (-1, idx, Item('b')))
idx += 1
heapq.heappush(pq, (-2, idx, Item('vip')))
idx += 1

print("目前 pq =", pq)

while pq:
    priority, order, item = heapq.heappop(pq)
    print("pop ->", "priority:", priority, "order:", order, "item:", item)
