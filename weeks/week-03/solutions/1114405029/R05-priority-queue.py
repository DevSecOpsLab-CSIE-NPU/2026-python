# R5. 優先佇列 PriorityQueue（1.5）

import heapq

class PriorityQueue:
    """
    實作一個優先權佇列，讓優先權較高的元素先被彈出。
    """
    def __init__(self):
        # 初始化一個空列表，用於存放堆疊 (Heap) 資料
        self._queue = []
        # 初始化一個遞增的序列號，用於處理優先權相同時的比較邏輯
        self._index = 0

    def push(self, item, priority):
        """
        將元素存入佇列。
        - priority: 數值越大，優先權越高。
        - item: 要存入的資料物件。
        """
        # heapq 預設是「最小堆疊」(Min-Heap)，會先彈出最小的值。
        # 1. 為了讓「高數字」先出，我們存入 -priority (取負號)。
        # 2. 存入 self._index 確保當優先權相同時，會按照「存入順序」排序。
        # 3. 存入 item 則是實際要取出的資料。
        heapq.heappush(self._queue, (-priority, self._index, item))
        
        # 每次存入後，遞增序列號
        self._index += 1

    def pop(self):
        """
        彈出並回傳優先權最高的元素。
        """
        # heappop 會回傳元組 (-priority, index, item)
        # 我們只需要最後一個元素 [ -1 ]，即原始存入的 item
        return heapq.heappop(self._queue)[-1]