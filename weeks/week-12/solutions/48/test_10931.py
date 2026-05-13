"""
UVA 10931 — Parity 測試程式
測試用例：計算整數二進位表示中1的個數（奇偶性）
"""

import unittest
from solution_10931 import calculate_parity


class TestParity(unittest.TestCase):
    """測試 Parity 問題的解決方案"""

    def test_case_1(self):
        """測試用例 1: 1 => 二進位 1, 1個1"""
        result = calculate_parity(1)
        self.assertEqual(result, "The parity of 1 is 1 (mod 2).")

    def test_case_2(self):
        """測試用例 2: 2 => 二進位 10, 1個1"""
        result = calculate_parity(2)
        self.assertEqual(result, "The parity of 10 is 1 (mod 2).")

    def test_case_3(self):
        """測試用例 3: 10 => 二進位 1010, 2個1"""
        result = calculate_parity(10)
        self.assertEqual(result, "The parity of 1010 is 2 (mod 2).")

    def test_case_4(self):
        """測試用例 4: 21 => 二進位 10101, 3個1"""
        result = calculate_parity(21)
        self.assertEqual(result, "The parity of 10101 is 3 (mod 2).")

    def test_case_5(self):
        """測試用例 5: 255 => 二進位 11111111, 8個1"""
        result = calculate_parity(255)
        self.assertEqual(result, "The parity of 11111111 is 8 (mod 2).")

    def test_case_6(self):
        """測試用例 6: 7 => 二進位 111, 3個1"""
        result = calculate_parity(7)
        self.assertEqual(result, "The parity of 111 is 3 (mod 2).")

    def test_case_7(self):
        """測試用例 7: 100 => 二進位 1100100, 3個1"""
        result = calculate_parity(100)
        self.assertEqual(result, "The parity of 1100100 is 3 (mod 2).")


if __name__ == "__main__":
    unittest.main()
