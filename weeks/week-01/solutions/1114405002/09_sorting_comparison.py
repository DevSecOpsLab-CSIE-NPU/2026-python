import unittest
from operator import itemgetter

# 測試類別：測試比較、排序與 key 函式
# 這個類別包含測試比較運算符、排序函數和 key 參數的單元測試
class TestSortingComparison(unittest.TestCase):

    # 測試方法：測試 tuple 比較順序
    # Tuple 比較是按元素順序比較，這裡測試 (1,2) < (1,3) 因為第二個元素 2 < 3
    def test_tuple_comparison(self):
        # 定義兩個 tuple
        a = (1, 2)
        b = (1, 3)
        # 斷言 a 小於 b，因為第一個元素相等，第二個元素 2 < 3
        self.assertTrue(a < b)

    # 測試方法：測試 sorted 函數使用 key 參數
    # sorted 函數可以接受 key 函數來自定義排序依據，這裡用 lambda 函數按 'price' 排序
    def test_sorted_with_key(self):
        # 準備測試資料：字典列表
        data = [{'price': 10}, {'price': 5}, {'price': 20}]
        # 使用 sorted 函數，按 'price' 鍵排序
        result = sorted(data, key=lambda x: x['price'])
        # 預期結果：按價格升序排列
        expected = [{'price': 5}, {'price': 10}, {'price': 20}]
        # 斷言結果等於預期
        self.assertEqual(result, expected)

    # 測試方法：測試 min 函數使用 key 參數
    # min 函數同樣可以使用 key 參數，這裡使用 itemgetter 來獲取 'uid' 鍵
    def test_min_with_key(self):
        # 準備測試資料：字典列表
        data = [{'uid': 2}, {'uid': 1}, {'uid': 3}]
        # 使用 min 函數，按 'uid' 鍵找到最小值
        result = min(data, key=itemgetter('uid'))
        # 預期結果：uid 最小的字典
        expected = {'uid': 1}
        # 斷言結果等於預期
        self.assertEqual(result, expected)

    # 測試方法：測試 (priority, index, item) 可排序
    # Tuple 可以按多個條件排序，這裡測試優先級、索引和項目的排序
    def test_priority_tuple_sorting(self):
        # 準備測試資料：包含優先級、索引和項目的 tuple 列表
        items = [(2, 1, 'b'), (1, 2, 'a'), (2, 0, 'c')]
        # 使用 sorted 函數排序，tuple 會按第一個元素、第二個元素等順序比較
        result = sorted(items)
        # 預期結果：先按優先級排序，相同優先級再按索引排序
        expected = [(1, 2, 'a'), (2, 0, 'c'), (2, 1, 'b')]
        # 斷言結果等於預期
        self.assertEqual(result, expected)

# 如果直接運行此檔案，執行所有測試
if __name__ == '__main__':
    unittest.main()