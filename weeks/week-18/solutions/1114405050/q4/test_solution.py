import unittest
from solution import linear_search, binary_search

class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        self.sorted_arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
        self.target = 138 # 假設目標為 100 + 50 (學號末兩碼) = 150 -> 這裡先測 130 看看

    def test_binary_search_found(self):
        # 測試二分搜尋找到目標
        found, idx, count = binary_search(self.sorted_arr, 130)
        self.assertTrue(found)
        self.assertEqual(idx, 12)
        self.assertLessEqual(count, 4) # log2(15) ~ 3.9

    def test_binary_search_not_found(self):
        # 測試二分搜尋沒找到目標
        found, idx, count = binary_search(self.sorted_arr, 138)
        self.assertFalse(found)
        self.assertEqual(idx, -1)

    def test_linear_search_found(self):
        # 測試線性搜尋找到目標
        found, idx, count = linear_search(self.sorted_arr, 130)
        self.assertTrue(found)
        self.assertEqual(idx, 12)
        self.assertEqual(count, 13) # 第 13 個元素

if __name__ == '__main__':
    unittest.main()
