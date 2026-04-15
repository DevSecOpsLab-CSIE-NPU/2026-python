# U5. 優先佇列為何要加 index（1.5）

# 優先佇列（heapq）在比較元素時，會使用以下策略：
# 1. 先比較第一個元素（priority 值）
# 2. 若第一個相同，再比較第二個元素
# 3. 若還相同，再比較第三個元素，依此類推
#
# 問題：若自訂物件不支援 < （小於）運算，會拋出 TypeError。

import heapq

class Item:
    def __init__(self, name):
        self.name = name
    # 注意：Item 沒有定義 __lt__() 方法，所以無法進行 < 比較

pq = []

# 錯誤做法：只放 (priority, item)
# 當兩筆資料的 priority 相同時（如都是 -1），
# heapq 會試圖比較 Item 物件，但 Item 未實作 < 運算，結果拋 TypeError。
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError: '<' not supported between instances of 'Item' and 'Item'

# 正確做法：在 priority 和 item 之間加上 index
# - idx 是插入順序的計數器
# - (priority, idx, item) 三元組：
#   - priority 相同時，heapq 會比較 idx（總是能比較數字）
#   - idx 同時記錄了插入順序，確保同 priority 時保持 FIFO（先入先出）
idx = 0
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1

# 此時 pq 的內部結構會是最小堆，最頂端的元素為最高優先級
# (priority=-1, idx=0, Item object) 會排在最頂端
print(heapq)  # 這會列印整個堆相關資訊

# 補充觀念：
# - 用負數表示 priority 時，-1 > -2，所以 -1 優先級更低（數值小優先級高）
# - index 的技巧不只適用 heapq，也常用在其他需要 tie-break 的氣況
# - 若需要比較自訂物件本身，應在 Item 類別中實作 __lt__() 等特殊方法