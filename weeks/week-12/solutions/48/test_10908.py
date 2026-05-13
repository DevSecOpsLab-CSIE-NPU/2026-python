"""
UVA 10908 — Largest Square 測試程式
測試用例：給定字元網格和中心點，找最大同色正方形邊長
"""

import unittest
from solution_10908 import find_largest_square_size


class TestLargestSquare(unittest.TestCase):
    """測試 Largest Square 問題的解決方案"""

    def setUp(self):
        """設置測試用的網格"""
        self.grid = [
            "abbbaaaaaa",
            "abbbaaaaaa",
            "abbbaaaaaa",
            "aaaaaaaaaa",
            "aaaaaaaaaa",
            "aaccaaaaaa",
            "aaccaaaaaa"
        ]

    def test_case_1(self):
        """測試用例 1: 中心 (1, 2) => 邊長 3"""
        result = find_largest_square_size(self.grid, 1, 2)
        self.assertEqual(result, 3)

    def test_case_2(self):
        """測試用例 2: 中心 (2, 4) => 邊長 1"""
        result = find_largest_square_size(self.grid, 2, 4)
        self.assertEqual(result, 1)

    def test_case_3(self):
        """測試用例 3: 中心 (4, 6) => 邊長 5"""
        result = find_largest_square_size(self.grid, 4, 6)
        self.assertEqual(result, 5)

    def test_case_4(self):
        """測試用例 4: 中心 (5, 2) => 邊長 1"""
        result = find_largest_square_size(self.grid, 5, 2)
        self.assertEqual(result, 1)

    def test_case_5(self):
        """測試用例 5: 單一字元正方形"""
        small_grid = ["abc", "def", "ghi"]
        result = find_largest_square_size(small_grid, 1, 1)
        self.assertEqual(result, 1)

    def test_case_6(self):
        """測試用例 6: 整個網格相同字元"""
        uniform_grid = ["aaa", "aaa", "aaa"]
        result = find_largest_square_size(uniform_grid, 1, 1)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
