"""UVA 11417 GCD — 單元測試

測試目標：sum_of_gcd(n) 計算 1 <= i < j <= n 範圍內所有 gcd(i, j) 的總和。

此檔案包含多個測試案例，並以繁體中文註解說明每個 case 的意義。
"""

import unittest

# 完成 gcd.py 後，匯入 sum_of_gcd
from gcd import sum_of_gcd


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_1(self):
        # edge case：n=1 時沒有任何 i<j 的配對，總和應為 0
        self.assertEqual(sum_of_gcd(1), 0)

    def test_n_equals_2(self):
        # 最小有效範圍 1..2，只有一組 gcd(1,2) = 1
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_10(self):
        # UVA 題目常見範例：1..10 的 gcd 總和應為 67
        self.assertEqual(sum_of_gcd(10), 67)

    def test_n_equals_100(self):
        # 測試較大數值，確認演算法結果與已知答案一致
        self.assertEqual(sum_of_gcd(100), 13015)


if __name__ == "__main__":
    unittest.main()
