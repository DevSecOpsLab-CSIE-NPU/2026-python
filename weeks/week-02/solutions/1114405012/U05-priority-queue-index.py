# U5. 優先佇列為何要加 index（1.5）
#
# 觀念重點：
# - heapq 會比較 tuple：先比第 1 個，再比第 2 個，以此類推。
# - 若 priority 相同，會嘗試比較 item 物件本身，可能觸發 TypeError。
# - 加入遞增 index 作為第二排序鍵，就能避免比較 item。

import heapq


class Item:
    def __init__(self, name):
        self.name = name


pq = []

# 若只放 (priority, item)，當 priority 相同時會比較 Item，通常會噴 TypeError。
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError

# 正解：放 (priority, index, item)
# - priority：主要排序鍵（這裡用負值模擬「數字越大優先度越高」）
# - index：同 priority 時的穩定排序鍵（先進先出）
# - item：真正資料
idx = 0
heapq.heappush(pq, (-1, idx, Item('a')))
idx += 1
heapq.heappush(pq, (-1, idx, Item('b')))
idx += 1
