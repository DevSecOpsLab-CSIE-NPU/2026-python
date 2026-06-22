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
        self.assertEqual(cmp, 10)  # 118 在索引 117, 二分搜尋路徑: mid=499→249→124→61→92→108→116→120→118→117 = 10 次

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
