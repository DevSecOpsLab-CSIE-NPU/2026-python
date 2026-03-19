# U5. 優先佇列為何要加 index（範例 1.5）
# 原理：當兩個元素優先級相同時，heapq 會嘗試比較元素本身。若元素不支援比較（如自定義物件），程式會崩潰。

import heapq

class Item:
    def __init__(self, name):
        self.name = name

pq = []
# 解決方案：加入一個遞增的 index 放在中間 (priority, index, item)
# 這樣當 priority 相同時，會先比較 index，而不會去比較 Item 物件。
idx = 0
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1