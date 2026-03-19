"""U05: priority 相同時，加入 index 避免比較 item 本體。"""

import heapq


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Item({self.name})'


pq = []
index = 0

# 三元組格式: (priority, index, item)
# priority 相同時，會改比 index，不會去比 Item 物件本身
heapq.heappush(pq, (-1, index, Item('a')))
index += 1
heapq.heappush(pq, (-1, index, Item('b')))
index += 1
heapq.heappush(pq, (-2, index, Item('c')))

while pq:
    print('pop:', heapq.heappop(pq))
