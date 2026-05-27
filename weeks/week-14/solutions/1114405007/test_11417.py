"""
題目 11417 - GCD (最大公因數總和) 測試程式
計算所有 1 ≤ i < j ≤ N 的數對之 GCD 的總和
"""

import unittest
from solution_11417 import gcd, sum_of_gcd


class TestGCD(unittest.TestCase):
    """GCD 相關函數的單元測試"""

    def test_gcd_basic(self):
        """測試基本的 GCD 計算"""
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(5, 3), 1)
        self.assertEqual(gcd(100, 50), 50)

    def test_gcd_same_number(self):
        """測試相同數字的 GCD"""
        self.assertEqual(gcd(7, 7), 7)
        self.assertEqual(gcd(1, 1), 1)

    def test_gcd_with_one(self):
        """測試與 1 的 GCD"""
        self.assertEqual(gcd(1, 5), 1)
        self.assertEqual(gcd(10, 1), 1)

    def test_sum_of_gcd_n2(self):
        """測試 N=2 的情況"""
        # gcd(1,2) = 1
        self.assertEqual(sum_of_gcd(2), 1)

    def test_sum_of_gcd_n3(self):
        """測試 N=3 的情況"""
        # gcd(1,2) + gcd(1,3) + gcd(2,3) = 1 + 1 + 1 = 3
        self.assertEqual(sum_of_gcd(3), 3)

    def test_sum_of_gcd_n10(self):
        """測試 N=10 的情況（題目範例）"""
        # 預期結果：67
        self.assertEqual(sum_of_gcd(10), 67)

    def test_sum_of_gcd_n100(self):
        """測試 N=100 的情況（題目範例）"""
        # 預期結果：13015
        self.assertEqual(sum_of_gcd(100), 13015)

    def test_sum_of_gcd_n500(self):
        """測試 N=500 的情況（題目範例）"""
        # 預期結果：442011
        self.assertEqual(sum_of_gcd(500), 442011)

    def test_sum_of_gcd_n5(self):
        """測試 N=5 的情況"""
        # gcd(1,2) + gcd(1,3) + gcd(1,4) + gcd(1,5) +
        # gcd(2,3) + gcd(2,4) + gcd(2,5) +
        # gcd(3,4) + gcd(3,5) +
        # gcd(4,5) = 1+1+1+1 + 1+2+1 + 1+1 + 1 = 11
        self.assertEqual(sum_of_gcd(5), 11)


if __name__ == '__main__':
    unittest.main()
