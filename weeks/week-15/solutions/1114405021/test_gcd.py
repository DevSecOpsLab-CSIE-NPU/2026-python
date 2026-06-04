"""UVA 11417 GCD — 測試骨架

題目：sum_of_gcd(n) 計算 1 <= i < j <= n 範圍內所有 gcd(i, j) 的總和。

待辦：
  1. 跟 AI 討論，補齊至少 3 個 test case（含 1 個 edge case）
  2. 跑 `python -m unittest test_gcd.py` 確認全部紅燈
  3. commit: "test: add failing tests for UVA 11417 GCD"
  4. 再去寫 gcd.py
"""

import unittest

# 嘗試從 gcd 模組匯入，尚未實作時設為 None 以便跳過測試
try:
    from gcd import sum_of_gcd  # 完成 gcd.py 後解除註解
except Exception:
    sum_of_gcd = None


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_2(self):
        # TODO: gcd(1,2) = 1，總和應為 1
        if sum_of_gcd is None:
            self.skipTest("`gcd.sum_of_gcd` not implemented")
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_10(self):
        # TODO: 範例答案 67
        if sum_of_gcd is None:
            self.skipTest("`gcd.sum_of_gcd` not implemented")
        self.assertEqual(sum_of_gcd(10), 67)

    def test_edge_case(self):
        # TODO: 想一個 edge case（提示：n=1 時應為多少？）
        if sum_of_gcd is None:
            self.skipTest("`gcd.sum_of_gcd` not implemented")
        # edge case: n=1 時沒有任何 (i,j) pair，總和為 0
        self.assertEqual(sum_of_gcd(1), 0)


if __name__ == "__main__":
    unittest.main()
