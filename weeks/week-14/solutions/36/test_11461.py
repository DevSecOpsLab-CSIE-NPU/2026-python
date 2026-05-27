# Square Numbers 測試程式
# 題目 11461: UVA — Square Numbers
# 計算區間 [a, b] 中完全平方數的個數

import unittest
import math

# 匯入解答程式
import sys
sys.path.insert(0, '.')
from q11461 import count_squares

class TestSquareNumbers(unittest.TestCase):
    """完全平方數計算測試類"""
    
    def test_simple_cases(self):
        """測試簡單案例"""
        # 測試 [1, 4]：1, 4 都是完全平方數
        self.assertEqual(count_squares(1, 4), 2)
        
        # 測試 [1, 10]：1, 4, 9 都是完全平方數
        self.assertEqual(count_squares(1, 10), 3)
        
    def test_single_perfect_square(self):
        """測試單一完全平方數"""
        # 測試 [9, 9]：只有9本身
        self.assertEqual(count_squares(9, 9), 1)
        
        # 測試 [10, 15]：沒有完全平方數
        self.assertEqual(count_squares(10, 15), 0)
        
    def test_large_range(self):
        """測試大範圍"""
        # 測試 [1, 100000]：應該有 316 個完全平方數
        self.assertEqual(count_squares(1, 100000), 316)
        
    def test_perfect_squares_only(self):
        """測試完全平方數之間的區間"""
        # 測試 [4, 25]：4, 9, 16, 25 共4個
        self.assertEqual(count_squares(4, 25), 4)

if __name__ == '__main__':
    unittest.main()
