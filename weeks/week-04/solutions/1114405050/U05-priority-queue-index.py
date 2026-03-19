# U5. 優先佇列為何要加 index（1.5）
"""
本範例示範使用 heapq 實作優先佇列（priority queue）時，
為什麼在 tuple 裡加入 index（或排序鍵）很重要。

heapq 在比較元素時，預設會比較 tuple 的每個成員：
1) 先比較 tuple[0]，若相同再比較 tuple[1]，以此類推。
2) 因此若 tuple[0]（優先權）相同，heapq 會嘗試比較 tuple[1]。
3) 若 tuple[1] 是自訂物件（例如 Item），而該物件未實作 __lt__，
   就會拋出 TypeError，導致 heapq 失敗。

解法是將「可比較的索引（通常為遞增的整數）」放在優先權之後，
這樣即使優先權相同，也能透過索引維持穩定排序（先進先出）。
"""

import heapq

class Item:
    def __init__(self, name):
        self.name = name

# 優先佇列底層結構是 heap（最小堆），因此 smallest element 會先被 pop
# 以 (-priority, idx, item) 的形式存放，可讓高優先權（大的 priority）先出列
pq = []

# 若只用 (priority, item) 的話：
# 當 priority 相同時，heapq 會比較 item；
# 若 item 是自訂物件而沒有實作 __lt__，會拋出 TypeError。
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError: '<' not supported

# 正確做法：加上可比較的 index，避免直接比較 item
idx = 0
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1

# 這樣即使 priority 相同，也會依照 idx 先後順序決定出列順序

