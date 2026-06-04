"""UVA 11417 GCD — 測試骨架

題目：sum_of_gcd(n) 計算 1 <= i < j <= n 範圍內所有 gcd(i, j) 的總和。

待辦：
  1. 跟 AI 討論，補齊至少 3 個 test case（含 1 個 edge case）
  2. 跑 `python -m unittest test_gcd.py` 確認全部紅燈
  3. commit: "test: add failing tests for UVA 11417 GCD"
  4. 再去寫 gcd.py
"""

import unittest

from gcd import sum_of_gcd  # 完成 gcd.py 後解除註解


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_1(self):
        """Edge case: 當 n=1 時，沒有 i < j 的配對，總和應為 0"""
        self.assertEqual(sum_of_gcd(1), 0)

    def test_n_equals_2(self):
        """基本案例: gcd(1,2)=1，總和應為 1"""
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_3(self):
        """中等案例: gcd(1,2)=1, gcd(1,3)=1, gcd(2,3)=1，總和應為 3"""
        self.assertEqual(sum_of_gcd(3), 3)

    def test_n_equals_10(self):
        """題目範例: 結果應為 67"""
        self.assertEqual(sum_of_gcd(10), 67)


if __name__ == "__main__":
    unittest.main()
