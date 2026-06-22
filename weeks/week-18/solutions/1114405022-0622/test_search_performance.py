import unittest
from search_performance import linear_search, binary_search


class TestSearchPerformance(unittest.TestCase):

    def test_linear_search_found(self):
        # 測試線性搜尋：找到目標
        data = [10, 20, 30, 40, 50]
        target = 30
        index, cmp = linear_search(data, target)
        self.assertEqual(index, 2)
        self.assertEqual(cmp, 3)

    def test_linear_search_not_found(self):
        # 測試線性搜尋：找不到目標
        data = [10, 20, 30]
        target = 40
        index, cmp = linear_search(data, target)
        self.assertEqual(index, -1)
        self.assertEqual(cmp, 3)

    def test_binary_search_found(self):
        # 測試二分搜尋：找到目標
        data = [10, 20, 30, 40, 50, 60, 70]
        target = 20
        index, cmp = binary_search(data, target)
        self.assertEqual(index, 1)
        self.assertGreater(cmp, 0)
        self.assertLessEqual(cmp, 3) # log2(7) approx 2.8

    def test_binary_search_not_found(self):
        # 測試二分搜尋：找不到目標
        data = [10, 20, 30, 40, 50]
        target = 25
        index, cmp = binary_search(data, target)
        self.assertEqual(index, -1)

    def test_binary_search_unsorted_raises_valueerror(self):
        # 測試未排序資料拋出 ValueError
        data = [30, 10, 20]
        target = 20
        with self.assertRaises(ValueError):
            binary_search(data, target)

    def test_empty_list(self):
        # 測試空 list 邊界
        target = 122
        self.assertEqual(linear_search([], target), (-1, 0))
        self.assertEqual(binary_search([], target), (-1, 0))


if __name__ == "__main__":
    unittest.main()
