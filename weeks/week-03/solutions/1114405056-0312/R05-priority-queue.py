# R5. 優先佇列 PriorityQueue（1.5）
# =========================================================
# 優先佇列是一種每個元素都有優先級的抽象資料類型
# 高優先級的元素會先被取出，而非先進先出
# 這裡使用 heapq 實現，最大優先級（數值大的）先出列
# =========================================================

import heapq

class PriorityQueue:
    """
    優先佇列類別

    使用最小堆實現，但通過將優先級取負數來實現最大優先級先出
    _index 用於處理優先級相同時的元素順序問題（確保先進先出）
    """

    def __init__(self):
        # 內部使用列表作為堆的儲存結構
        self._queue = []
        # 計數器，用於記錄元素加入順序，解決同優先級的排序問題
        self._index = 0

    def push(self, item, priority):
        """
        將元素加入優先佇列

        Args:
            item: 要加入的元素
            priority: 優先級（數值越大優先級越高）

        使用負優先級（-priority）將最大值轉為最小堆中的「最小值」
        _index 遞增確保相同優先級時，較早加入的元素先被取出
        """
        # 堆中的每個元素是 (-priority, _index, item) 的元組
        # 第一個元素用於比較優先級（取負數實現最大堆效果）
        # 第二個元素確保 FIFO（相同優先級時）
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """
        移除並返回最高優先級的元素

        Returns:
            優先級最高的元素

        heappop 返回並移除堆中最小的元素（即我們的最大優先級元素）
        [-1] 取回原始的 item （元組的第三個元素）
        """
        return heapq.heappop(self._queue)[-1]
