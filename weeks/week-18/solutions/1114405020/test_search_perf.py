import unittest
from search_perf import binary_search_perf, linear_search_perf


class TestSearchPerf(unittest.TestCase):
    def test_binary_search_found(self):
        """測試二分搜尋成功找到目標"""
        data = list(range(0, 1000, 2))  # 0, 2, 4, ..., 998
        # 搜尋 120 (應在 index 60)
        found, idx, cmp = binary_search_perf(data, 120)
        self.assertTrue(found)
        self.assertEqual(idx, 60)
        self.assertGreater(cmp, 0)

    def test_binary_search_not_found(self):
        """測試二分搜尋找不到目標"""
        data = list(range(0, 1000, 2))
        # 搜尋 121 (奇數，不存在)
        found, idx, cmp = binary_search_perf(data, 121)
        self.assertFalse(found)
        self.assertEqual(idx, -1)
        self.assertGreater(cmp, 0)

    def test_linear_search_found(self):
        """測試線性搜尋成功找到目標"""
        data = list(range(0, 1000, 2))
        found, idx, cmp = linear_search_perf(data, 120)
        self.assertTrue(found)
        self.assertEqual(idx, 60)
        self.assertEqual(cmp, 61)  # 線性搜尋到 index 60 需要 61 次比較

    def test_empty_list(self):
        """測試空列表的邊界情況"""
        found, idx, cmp = binary_search_perf([], 120)
        self.assertFalse(found)
        self.assertEqual(idx, -1)
        self.assertEqual(cmp, 0)


if __name__ == "__main__":
    unittest.main()
