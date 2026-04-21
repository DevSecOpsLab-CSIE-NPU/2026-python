import unittest
import heapq
from collections import deque

# 自定義類別：User 類別
# 這個類別用來示範類別和物件的基本概念
class User:
    # 初始化方法：設定用戶 ID
    def __init__(self, user_id):
        self.user_id = user_id

# 測試類別：測試模組、類別、例外與 Big-O
# 這個類別包含測試 import、class、例外處理和基本 Big-O 概念的單元測試
class TestImportClassException(unittest.TestCase):

    # 測試方法：測試 import heapq
    # heapq 模組提供堆隊列演算法，這裡測試推入和彈出操作
    def test_import_heapq(self):
        # 創建一個空堆
        heap = []
        # 推入元素到堆中
        heapq.heappush(heap, 3)
        heapq.heappush(heap, 1)
        heapq.heappush(heap, 2)
        # 彈出最小元素，應該是 1
        self.assertEqual(heapq.heappop(heap), 1)

    # 測試方法：測試 import deque
    # deque 是雙端隊列，提供高效的兩端操作，這裡測試 append 和 appendleft
    def test_import_deque(self):
        # 創建一個 deque
        d = deque([1, 2, 3])
        # 在右端添加元素
        d.append(4)
        # 在左端添加元素
        d.appendleft(0)
        # 斷言最終列表為 [0, 1, 2, 3, 4]
        self.assertEqual(list(d), [0, 1, 2, 3, 4])

    # 測試方法：測試 class 與物件
    # 測試自定義類別的實例化和屬性訪問
    def test_class_user(self):
        # 創建 User 物件
        user = User(123)
        # 斷言用戶 ID 正確
        self.assertEqual(user.user_id, 123)

    # 測試方法：測試例外處理
    # 測試 try/except 區塊，這裡測試轉換字串到整數時的 ValueError
    def test_exception_handling(self):
        # 準備一個無法轉換為整數的字串
        val = 'abc'
        # 嘗試轉換，如果拋出 ValueError 則捕獲
        try:
            int(val)
            # 如果沒有拋出例外，測試失敗
            self.fail("應該拋出 ValueError")
        except ValueError:
            # 正確行為：捕獲到 ValueError
            pass  # 正確行為

    # 測試方法：測試基本 Big-O 觀念
    # Big-O 表示演算法的時間複雜度，這裡示範 deque 的 append 操作（通常 O(1)）
    def test_big_o_concept(self):
        # 創建一個空的 deque
        d = deque()
        # 進行多次 append 操作，示範 O(1) 時間複雜度
        for i in range(1000):
            d.append(i)
        # 斷言長度正確
        self.assertEqual(len(d), 1000)

# 如果直接運行此檔案，執行所有測試
if __name__ == '__main__':
    unittest.main()