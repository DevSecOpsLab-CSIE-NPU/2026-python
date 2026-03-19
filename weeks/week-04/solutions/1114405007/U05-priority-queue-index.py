# U5. 優先佇列為何要加 index（1.5）

import heapq

class Item:
    def __init__(self, name):
        self.name = name

# 用 list 搭配 heapq 來實作優先佇列
pq = []
# 若只放 (priority, item)，同 priority 會比較 item，Item 不支援 < 會炸
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError

# 正解：加上遞增 index，當 priority 相同時改比 index，不會去比 Item 物件
idx = 0
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1

while pq:
    priority, order, item = heapq.heappop(pq)
    print('priority =', priority, 'order =', order, 'item =', item.name)
