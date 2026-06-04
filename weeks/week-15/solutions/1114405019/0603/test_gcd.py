"""UVA 11417 GCD — 測試

題目：sum_of_gcd(n) 計算 1 <= i < j <= n 範圍內所有 gcd(i, j) 的總和。
"""

import unittest
from gcd import sum_of_gcd


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_1(self):
        # edge case：迴圈空轉，無任何 (i, j) 配對，結果應為 0
        self.assertEqual(sum_of_gcd(1), 0)

    def test_n_equals_2(self):
        # gcd(1, 2) = 1，唯一一對，總和應為 1
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_3(self):
        # gcd(1,2)=1, gcd(1,3)=1, gcd(2,3)=1 → 總和 3
        self.assertEqual(sum_of_gcd(3), 3)

    def test_n_equals_10(self):
        # 範例答案
        self.assertEqual(sum_of_gcd(10), 67)


if __name__ == "__main__":
    unittest.main()
