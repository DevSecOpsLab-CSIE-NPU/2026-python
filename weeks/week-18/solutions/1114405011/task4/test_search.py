import unittest

class TestBinarySearchAndEval(unittest.TestCase):
    def test_binary_search_found(self):
        """測試二分搜尋核心邏輯與比較次數計數（找到）"""
        # 沒有 search.py 時會觸發 ModuleNotFoundError 紅燈
        from search import binary_search_eval

        arr = [10, 20, 30, 40, 50, 111, 130]
        found, idx, cmp_count = binary_search_eval(arr, 111)
        self.assertTrue(found)
        self.assertEqual(idx, 5)
        self.assertGreater(cmp_count, 0)

    def test_binary_search_not_found_and_edges(self):
        """測試：目標不存在、以及目標在首/尾端的邊界"""
        from search import binary_search_eval

        arr = [10, 20, 30, 40, 50, 111, 130]

        found, idx, cmp_count = binary_search_eval(arr, 10)
        self.assertTrue(found)
        self.assertEqual(idx, 0)
        self.assertGreater(cmp_count, 0)

        found, idx, cmp_count = binary_search_eval(arr, 130)
        self.assertTrue(found)
        self.assertEqual(idx, len(arr) - 1)
        self.assertGreater(cmp_count, 0)

        found, idx, cmp_count = binary_search_eval(arr, 25)
        self.assertFalse(found)
        self.assertEqual(idx, -1)
        self.assertGreater(cmp_count, 0)

if __name__ == "__main__":
    unittest.main()