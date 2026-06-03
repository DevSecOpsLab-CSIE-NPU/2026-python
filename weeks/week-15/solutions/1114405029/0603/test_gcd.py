"""UVA 11417 GCD — 測試檔

題目：sum_of_gcd(n) 計算 1 <= i < j <= n 範圍內所有 gcd(i, j) 的總和。

本檔依照 TDD 流程：
1. 先寫測試
2. 先確認紅燈
3. 再建立 gcd.py 實作
"""

import unittest

from gcd import sum_of_gcd


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_1_edge_case(self):
        # n = 1 時，沒有任何 i < j 的組合，所以總和是 0
        self.assertEqual(sum_of_gcd(1), 0)

    def test_n_equals_2(self):
        # gcd(1, 2) = 1
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_3(self):
        # gcd(1,2)=1, gcd(1,3)=1, gcd(2,3)=1，總和 3
        self.assertEqual(sum_of_gcd(3), 3)

    def test_n_equals_4(self):
        # gcd(1,2)=1, gcd(1,3)=1, gcd(1,4)=1,
        # gcd(2,3)=1, gcd(2,4)=2, gcd(3,4)=1，總和 7
        self.assertEqual(sum_of_gcd(4), 7)

    def test_n_equals_10(self):
        # 題目範例：n = 10 時答案為 67
        self.assertEqual(sum_of_gcd(10), 67)


if __name__ == "__main__":
    unittest.main()