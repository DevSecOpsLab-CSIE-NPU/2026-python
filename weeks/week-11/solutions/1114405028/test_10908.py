"""
UVA 10908 — Largest Square 測試程式
測試用例：給定字元網格和中心點，找最大同色正方形邊長。
"""

import unittest
from solution_10908 import find_largest_square_size


class TestLargestSquare(unittest.TestCase):
    """測試 Largest Square 問題的解決方案。"""

    def setUp(self):
        self.grid = [
            "abbbaaaaaa",
            "abbbaaaaaa",
            "abbbaaaaaa",
            "aaaaaaaaaa",
            "aaaaaaaaaa",
            "aaccaaaaaa",
            "aaccaaaaaa",
        ]

    def test_case_1(self):
        result = find_largest_square_size(self.grid, 1, 2)
        self.assertEqual(result, 3)

    def test_case_2(self):
        result = find_largest_square_size(self.grid, 2, 4)
        self.assertEqual(result, 1)

    def test_case_3(self):
        result = find_largest_square_size(self.grid, 4, 6)
        self.assertEqual(result, 5)

    def test_case_4(self):
        result = find_largest_square_size(self.grid, 5, 2)
        self.assertEqual(result, 1)

    def test_case_5(self):
        small_grid = ["abc", "def", "ghi"]
        result = find_largest_square_size(small_grid, 1, 1)
        self.assertEqual(result, 1)

    def test_case_6(self):
        uniform_grid = ["aaa", "aaa", "aaa"]
        result = find_largest_square_size(uniform_grid, 1, 1)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
