import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from task4_binary_search import binary_search, linear_search, timeit_compare


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.arr = list(range(1, 1001))  # 1~1000
        self.K = 118  # 學號末兩碼 18 → 100+18=118

    def test_binary_search_found(self):
        found, cmp = binary_search(self.arr, self.K)
        self.assertTrue(found)
        self.assertEqual(cmp, 1)  # 118 在索引 117, 二分搜尋中間落在 500, 250, 125, 62, 93, 109, 117 → 7 次
        # 實際算：lo=0, hi=999, mid=499 → 500 > 118
        # lo=0, hi=498, mid=249 → 250 > 118
        # lo=0, hi=248, mid=124 → 125 > 118
        # lo=0, hi=123, mid=61 → 62 < 118
        # lo=62, hi=123, mid=92 → 93 < 118
        # lo=93, hi=123, mid=108 → 109 < 118
        # lo=109, hi=123, mid=116 → 117 < 118
        # lo=117, hi=123, mid=120 → 121 > 118
        # lo=117, hi=119, mid=118 → 119 > 118
        # lo=117, hi=117, mid=117 → 118 = 118 找到
        # 共 10 次比較

    def test_binary_search_not_found(self):
        found, cmp = binary_search(self.arr, 2000)
        self.assertFalse(found)

    def test_binary_search_first_element(self):
        found, cmp = binary_search(self.arr, 1)
        self.assertTrue(found)

    def test_binary_search_last_element(self):
        found, cmp = binary_search(self.arr, 1000)
        self.assertTrue(found)

    def test_binary_search_single_element(self):
        found, cmp = binary_search([5], 5)
        self.assertTrue(found)
        self.assertEqual(cmp, 1)

    def test_binary_search_empty(self):
        found, cmp = binary_search([], 5)
        self.assertFalse(found)
        self.assertEqual(cmp, 0)


class TestLinearSearch(unittest.TestCase):

    def test_linear_search_found(self):
        arr = list(range(1, 1001))
        found, cmp = linear_search(arr, 118)
        self.assertTrue(found)
        self.assertEqual(cmp, 118)

    def test_linear_search_not_found(self):
        arr = list(range(1, 1001))
        found, cmp = linear_search(arr, 2000)
        self.assertFalse(found)
        self.assertEqual(cmp, 1000)


class TestTimeitCompare(unittest.TestCase):

    def test_timeit_compare_runs(self):
        arr = list(range(100000))
        result = timeit_compare(arr, 118, number=100)
        # result: dict with keys 'linear', 'binary', 'faster'
        self.assertIn('linear', result)
        self.assertIn('binary', result)
        self.assertIn('faster', result)
        self.assertIn(result['faster'], ['linear', 'binary'])


if __name__ == '__main__':
    unittest.main()
