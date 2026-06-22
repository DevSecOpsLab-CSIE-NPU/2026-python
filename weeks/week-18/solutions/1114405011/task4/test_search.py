import unittest

class TestBinarySearchAndEval(unittest.TestCase):
    def test_binary_search_logic(self):
        """測試二分搜尋核心邏輯與比較次數計數"""
        # 沒有 search.py 時會觸發 ModuleNotFoundError 紅燈
        from search import binary_search_eval
        
        arr = [10, 20, 30, 40, 50, 111, 130]
        # 搜尋目標 K = 111
        found, idx, cmp_count = binary_search_eval(arr, 111)
        self.assertTrue(found)
        self.assertEqual(idx, 5)
        self.assertGreater(cmp_count, 0)

if __name__ == "__main__":
    unittest.main()