"""
問題：UVA 11461 — Square Numbers（完全平方數）
題目來源：https://zerojudge.tw/ShowProblem?problemid=d186

題意摘要：
給定兩個整數 a 和 b，求閉區間 [a, b] 中完全平方數（perfect square）
的個數。完全平方數是指平方根為整數的正整數，例如 1, 4, 9, ...
"""

import unittest

# 從解題程式中匯入被測試的函式
from p11461 import count_square_numbers


class TestSquareNumbers(unittest.TestCase):
    """UVA 11461 完全平方數個數的單元測試"""

    def test_1_to_4(self):
        """測試 [1, 4]：完全平方數有 1, 4 → 2 個"""
        self.assertEqual(count_square_numbers(1, 4), 2)

    def test_1_to_10(self):
        """測試 [1, 10]：完全平方數有 1, 4, 9 → 3 個"""
        self.assertEqual(count_square_numbers(1, 10), 3)

    def test_1_to_100000(self):
        """測試 [1, 100000]：最大範圍，sqrt(100000)≈316.22 → 316 個"""
        self.assertEqual(count_square_numbers(1, 100000), 316)

    def test_single_perfect_square(self):
        """測試區間只有一個完全平方數 [9, 9]"""
        self.assertEqual(count_square_numbers(9, 9), 1)

    def test_single_non_square(self):
        """測試區間沒有完全平方數 [10, 11]"""
        self.assertEqual(count_square_numbers(10, 11), 0)

    def test_no_square_in_range(self):
        """測試區間沒有完全平方數 [2, 3]"""
        self.assertEqual(count_square_numbers(2, 3), 0)

    def test_large_range_starting_from_non_square(self):
        """測試從非完全平方數起始的範圍 [5, 16]：有 9, 16 → 2 個"""
        self.assertEqual(count_square_numbers(5, 16), 2)


if __name__ == "__main__":
    unittest.main()
