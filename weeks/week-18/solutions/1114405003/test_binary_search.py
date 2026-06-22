"""
第四題 二分搜尋效能 - 測試檔案
學號: 1114405003
K = 100 + 03 = 103
"""
import unittest
from binary_search import linear_search, binary_search, generate_sorted_array


class TestBinarySearch(unittest.TestCase):
    """二分搜尋效能測試"""

    def test_found_middle(self):
        """找到中間元素"""
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        found, idx, cmp = binary_search(arr, 11)
        self.assertTrue(found)
        self.assertEqual(idx, 5)

    def test_not_found(self):
        """找不到"""
        arr = [1, 3, 5, 7, 9]
        found, idx, cmp = binary_search(arr, 4)
        self.assertFalse(found)
        self.assertEqual(idx, -1)

    def test_first_element(self):
        """找第一個元素"""
        arr = [1, 2, 3, 4, 5]
        found, idx, cmp = binary_search(arr, 1)
        self.assertTrue(found)
        self.assertEqual(idx, 0)

    def test_last_element(self):
        """找最後一個元素"""
        arr = [1, 2, 3, 4, 5]
        found, idx, cmp = binary_search(arr, 5)
        self.assertTrue(found)
        self.assertEqual(idx, 4)

    def test_empty_array(self):
        """空陣列"""
        found, idx, cmp = binary_search([], 1)
        self.assertFalse(found)
        self.assertEqual(idx, -1)

    def test_single_element_found(self):
        """單一元素找到"""
        found, idx, cmp = binary_search([5], 5)
        self.assertTrue(found)
        self.assertEqual(idx, 0)

    def test_single_element_not_found(self):
        """單一元素找不到"""
        found, idx, cmp = binary_search([5], 3)
        self.assertFalse(found)

    def test_linear_search_found(self):
        """線性搜尋找到"""
        arr = [1, 3, 5, 7, 9]
        found, idx, cmp = linear_search(arr, 7)
        self.assertTrue(found)
        self.assertEqual(idx, 3)

    def test_linear_search_not_found(self):
        """線性搜尋找不到"""
        arr = [1, 3, 5, 7, 9]
        found, idx, cmp = linear_search(arr, 4)
        self.assertFalse(found)

    def test_linear_search_first(self):
        """線性搜尋第一個"""
        arr = [1, 2, 3, 4, 5]
        found, idx, cmp = linear_search(arr, 1)
        self.assertTrue(found)
        self.assertEqual(idx, 0)
        self.assertEqual(cmp, 1)

    def test_linear_search_last(self):
        """線性搜尋最後一個"""
        arr = [1, 2, 3, 4, 5]
        found, idx, cmp = linear_search(arr, 5)
        self.assertTrue(found)
        self.assertEqual(idx, 4)
        self.assertEqual(cmp, 5)

    def test_generate_sorted_array(self):
        """產生排序陣列"""
        arr = generate_sorted_array(100)
        self.assertEqual(len(arr), 100)
        self.assertEqual(arr, sorted(arr))

    def test_large_array_binary(self):
        """大陣列二分搜尋"""
        arr = generate_sorted_array(100000)
        target = arr[50000]  # 確保目標在陣列中
        found, idx, cmp = binary_search(arr, target)
        self.assertTrue(found)
        self.assertEqual(idx, 50000)

    def test_large_array_linear(self):
        """大陣列線性搜尋"""
        arr = generate_sorted_array(100000)
        target = arr[50000]  # 確保目標在陣列中
        found, idx, cmp = linear_search(arr, target)
        self.assertTrue(found)
        self.assertEqual(idx, 50000)

    def test_binary_cmp_count(self):
        """二分搜尋比較次數合理"""
        arr = generate_sorted_array(1000)
        target = arr[500]  # 確保目標在陣列中
        found, idx, cmp = binary_search(arr, target)
        self.assertTrue(found)
        self.assertLessEqual(cmp, 20)  # log2(1000) ≈ 10

    def test_linear_cmp_count(self):
        """線性搜尋比較次數"""
        arr = generate_sorted_array(1000)
        target = arr[500]  # 確保目標在陣列中
        found, idx, cmp = linear_search(arr, target)
        self.assertTrue(found)
        self.assertEqual(idx, 500)
        self.assertEqual(cmp, 501)


if __name__ == "__main__":
    unittest.main()
