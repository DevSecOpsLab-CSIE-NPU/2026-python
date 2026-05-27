"""
題目 11461 - Square Numbers (完全平方數計數) 測試程式
計算閉區間 [a, b] 中完全平方數的個數
"""

import unittest
from solution_11461 import count_perfect_squares


class TestSquareNumbers(unittest.TestCase):
    """完全平方數計數函數的單元測試"""

    def test_single_perfect_square(self):
        """測試單一完全平方數"""
        self.assertEqual(count_perfect_squares(4, 4), 1)
        self.assertEqual(count_perfect_squares(1, 1), 1)
        self.assertEqual(count_perfect_squares(9, 9), 1)

    def test_no_perfect_squares(self):
        """測試沒有完全平方數的區間"""
        self.assertEqual(count_perfect_squares(2, 3), 0)
        self.assertEqual(count_perfect_squares(5, 8), 0)

    def test_multiple_perfect_squares(self):
        """測試包含多個完全平方數的區間"""
        # [1, 4]: 1, 4 = 2 個
        self.assertEqual(count_perfect_squares(1, 4), 2)
        # [1, 10]: 1, 4, 9 = 3 個
        self.assertEqual(count_perfect_squares(1, 10), 3)

    def test_example_1_4(self):
        """測試題目範例：[1, 4]"""
        # 完全平方數：1, 4 = 2 個
        self.assertEqual(count_perfect_squares(1, 4), 2)

    def test_example_1_10(self):
        """測試題目範例：[1, 10]"""
        # 完全平方數：1, 4, 9 = 3 個
        self.assertEqual(count_perfect_squares(1, 10), 3)

    def test_example_1_100000(self):
        """測試題目範例：[1, 100000]"""
        # 完全平方數：1² ~ 316² = 316 個
        # (因為 316² = 99856 < 100000 < 317² = 100489)
        self.assertEqual(count_perfect_squares(1, 100000), 316)

    def test_range_not_starting_at_one(self):
        """測試不從 1 開始的區間"""
        # [10, 20]: 16 = 1 個
        self.assertEqual(count_perfect_squares(10, 20), 1)
        # [50, 100]: 64, 81, 100 = 3 個
        self.assertEqual(count_perfect_squares(50, 100), 3)

    def test_large_numbers(self):
        """測試較大的數字"""
        # [1000, 2000]: 1024(32²), 1089(33²), ..., 1936(44²) = 13 個
        # 計算：floor(√2000) - floor(√999) = 44 - 31 = 13
        self.assertEqual(count_perfect_squares(1000, 2000), 13)

    def test_consecutive_perfect_squares(self):
        """測試連續的完全平方數"""
        # [4, 9]: 4, 9 = 2 個
        self.assertEqual(count_perfect_squares(4, 9), 2)
        # [16, 25]: 16, 25 = 2 個
        self.assertEqual(count_perfect_squares(16, 25), 2)


if __name__ == '__main__':
    unittest.main()
