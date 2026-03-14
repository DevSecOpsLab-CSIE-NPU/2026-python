# R5. 優先佇列 PriorityQueue（1.5）
#
# 這份程式示範如何用 heapq 自己包一個「優先佇列」類別。
# 優先佇列特性：
# - 每個項目都有 priority（優先級）
# - 取出時不是先進先出，而是「優先級高的先出」

import heapq


class PriorityQueue:
    def __init__(self):
        # _queue: 真正儲存資料的堆（list 形式）
        self._queue = []

        # _index: 遞增序號，當優先級相同時用來決定先後順序
        # 也可避免 Python 比較 item 本體時出現 TypeError（不同型別不可比）
        self._index = 0

    def push(self, item, priority):
        # heappush 放入 tuple: (-priority, _index, item)
        # 為什麼 priority 前面要加負號？
        # - heapq 是「最小堆」，會先彈出最小值
        # - 但我們想要「priority 越大越先出」
        # - 所以把 priority 變成負數，優先級越大 -> 負數越小 -> 越先被 pop
        #
        # tuple 比較順序是由左到右：
        # 1) 先比 -priority
        # 2) 若相同，再比 _index（先進來的 _index 較小，先出去）
        # 3) item 放最後，通常不參與排序比較
        heapq.heappush(self._queue, (-priority, self._index, item))

        # 每 push 一次就遞增，確保每筆資料有唯一插入順序
        self._index += 1

    def pop(self):
        # heappop 會回傳整個 tuple: (-priority, _index, item)
        # 我們只想回傳實際資料 item，所以取最後一個元素 [-1]
        return heapq.heappop(self._queue)[-1]


# 讀懂這份程式的步驟：
# 1. 先記住 heapq 預設是最小堆，因此會先拿「最小鍵值」。
# 2. 想做「最大優先級先出」，就把 priority 轉為負值。
# 3. 同優先級時用 _index 當 tie-break，讓順序穩定且可預期。
# 4. push/pop 本質都在操作 tuple 鍵值，item 只是被一起帶著走。
