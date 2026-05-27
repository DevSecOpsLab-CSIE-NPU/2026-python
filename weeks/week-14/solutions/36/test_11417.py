# GCD 測試程式
# 題目 11417: UVA — GCD
# 計算所有數對 (i, j) 的 GCD 總和，其中 1 <= i < j <= N

import unittest
import math

# 匯入解答程式
import sys
sys.path.insert(0, '.')
from q11417 import sum_of_gcds

class TestGCDSum(unittest.TestCase):
    """GCD 總和計算測試類"""
    
    def test_small_numbers(self):
        """測試小數字"""
        # N=10: 所有 (i,j) 的 gcd 總和
        # 計算: gcd(1,2)+gcd(1,3)+...+gcd(9,10)
        result = sum_of_gcds(10)
        self.assertEqual(result, 67)
        
    def test_medium_number(self):
        """測試中等數字"""
        # N=100
        result = sum_of_gcds(100)
        self.assertEqual(result, 13015)
        
    def test_large_number(self):
        """測試大數字"""
        # N=500
        result = sum_of_gcds(500)
        self.assertEqual(result, 442011)
        
    def test_small_n(self):
        """測試最小的 N"""
        # N=2: 只有 gcd(1,2) = 1
        result = sum_of_gcds(2)
        self.assertEqual(result, 1)
        
    def test_n_equals_3(self):
        """測試 N=3"""
        # N=3: gcd(1,2) + gcd(1,3) + gcd(2,3) = 1 + 1 + 1 = 3
        result = sum_of_gcds(3)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
