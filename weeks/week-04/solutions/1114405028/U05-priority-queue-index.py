# U5. 優先佇列為何要加 index（1.5）

import heapq  # heapq 實作的優先佇列依靠 tuple 的字典序比較

class Item:
    def __init__(self, name):
        self.name = name  # 自訂類別，未定義 __lt__，無法直接比較大小

pq = []
# 若只放 (priority, item)，同 priority 會比較 item，Item 不支援 < 會炸
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError：Item 不支援比較

# 正解：加 index 避免比較 item
# tuple 比較時：先比 priority，相同再比 index，index 必定唯一，不會到第三位
idx = 0
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1  # 負號讓大 priority 先出列
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1
