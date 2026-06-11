"""
UVA 10931 — Parity 測試程式
測試用例：計算整數二進位表示中 1 的個數。
"""

import unittest
from solution_10931 import calculate_parity


class TestParity(unittest.TestCase):
    """測試 Parity 問題的解決方案。"""

    def test_case_1(self):
        self.assertEqual(calculate_parity(1), "The parity of 1 is 1 (mod 2).")

    def test_case_2(self):
        self.assertEqual(calculate_parity(2), "The parity of 10 is 1 (mod 2).")

    def test_case_3(self):
        self.assertEqual(calculate_parity(10), "The parity of 1010 is 2 (mod 2).")

    def test_case_4(self):
        self.assertEqual(calculate_parity(21), "The parity of 10101 is 3 (mod 2).")

    def test_case_5(self):
        self.assertEqual(calculate_parity(255), "The parity of 11111111 is 8 (mod 2).")

    def test_case_6(self):
        self.assertEqual(calculate_parity(7), "The parity of 111 is 3 (mod 2).")

    def test_case_7(self):
        self.assertEqual(calculate_parity(100), "The parity of 1100100 is 3 (mod 2).")


if __name__ == "__main__":
    unittest.main()
