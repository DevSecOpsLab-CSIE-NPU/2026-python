"""
問題：UVA 11417 — GCD（最大公因數總和）
題目來源：https://zerojudge.tw/ShowProblem?problemid=b410

題意摘要：
給定正整數 N，計算所有滿足 1 <= i < j <= N 的整數數對之
GCD（最大公因數）的總和：
  G = sum_{i=1}^{N-1} sum_{j=i+1}^{N} gcd(i, j)
"""

import unittest

# 從解題程式中匯入被測試的函式
from p11417 import gcd_sum


class TestGCDSum(unittest.TestCase):
    """UVA 11417 GCD 總和的單元測試"""

    def test_n_10(self):
        """測試 N=10，預期輸出 67"""
        self.assertEqual(gcd_sum(10), 67)

    def test_n_100(self):
        """測試 N=100，預期輸出 13015"""
        self.assertEqual(gcd_sum(100), 13015)

    def test_n_500(self):
        """測試 N=500，預期輸出 442011"""
        self.assertEqual(gcd_sum(500), 442011)

    def test_n_2(self):
        """測試最小邊界 N=2，唯一數對 (1,2) 的 gcd=1"""
        self.assertEqual(gcd_sum(2), 1)

    def test_n_3(self):
        """測試 N=3：數對 (1,2)=1, (1,3)=1, (2,3)=1，總和=3"""
        self.assertEqual(gcd_sum(3), 3)

    def test_n_5(self):
        """測試 N=5，手算驗證"""
        # (1,2)=1 (1,3)=1 (1,4)=1 (1,5)=1
        # (2,3)=1 (2,4)=2 (2,5)=1
        # (3,4)=1 (3,5)=1
        # (4,5)=1 → 總和 = 11
        self.assertEqual(gcd_sum(5), 11)


if __name__ == "__main__":
    unittest.main()
