import unittest
import os
import sys

# 確保能匯入同目錄下的 gcd.py
sys.path.insert(0, os.path.dirname(__file__))

from gcd import sum_of_gcd


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_2(self):
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_10(self):
        self.assertEqual(sum_of_gcd(10), 67)

    def test_n_equals_1_edge_case(self):
        self.assertEqual(sum_of_gcd(1), 0)

    def test_invalid_input_raises(self):
        # 驗證 n <= 0 應該視為無效輸入並丟出 ValueError
        with self.assertRaises(ValueError):
            sum_of_gcd(0)


if __name__ == "__main__":
    unittest.main()
