# R5. 優先佇列 PriorityQueue（1.5）
# 優先佇列是一種特殊的資料結構，
# 其中每個元素都有一個優先權，元素會按照優先權的順序被處理。
# 在 Python 中，可以使用 heapq 模組來實現優先佇列。

# 匯入 heapq 模組，用於堆積操作
import heapq

# 定義一個 PriorityQueue 類別
class PriorityQueue:
    # 初始化方法
    def __init__(self):
        # 使用列表來儲存堆積中的元素
        self._queue = []
        # 使用索引來處理相同優先權的情況，確保先進先出
        self._index = 0

    # 推入元素的方法，參數為項目和優先權
    def push(self, item, priority):
        # 使用負優先權來實現最大堆（因為 heapq 是最小堆）
        # 同時包含索引來處理相同優先權的穩定性
        heapq.heappush(self._queue, (-priority, self._index, item))
        # 增加索引，為下一個元素做準備
        self._index += 1

    # 彈出最高優先權元素的方法
    def pop(self):
        # 彈出堆積中最小的元素（由於負優先權，實際上是最大的優先權）
        # 返回元組中的最後一個元素，即原始項目
        return heapq.heappop(self._queue)[-1]
