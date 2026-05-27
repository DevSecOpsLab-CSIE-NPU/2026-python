# Symmetric Matrix 測試程式
# 題目 11349: UVA — Symmetric Matrix
# 判斷矩陣是否為中心對稱矩陣

import unittest

# 匯入解答程式
import sys
sys.path.insert(0, '.')
from q11349 import is_symmetric_matrix

class TestSymmetricMatrix(unittest.TestCase):
    """對稱矩陣判斷測試類"""
    
    def test_symmetric_matrix_3x3(self):
        """測試 3x3 的對稱矩陣"""
        # 測試範例1
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [3, 1, 5]
        ]
        self.assertTrue(is_symmetric_matrix(matrix))
        
    def test_non_symmetric_matrix_3x3(self):
        """測試 3x3 的非對稱矩陣"""
        # 測試範例2
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [0, 1, 5]
        ]
        self.assertFalse(is_symmetric_matrix(matrix))
        
    def test_single_element(self):
        """測試 1x1 矩陣"""
        matrix = [[5]]
        self.assertTrue(is_symmetric_matrix(matrix))
        
    def test_symmetric_2x2(self):
        """測試 2x2 的對稱矩陣"""
        matrix = [
            [1, 2],
            [2, 1]
        ]
        self.assertTrue(is_symmetric_matrix(matrix))
        
    def test_negative_values(self):
        """測試包含負數的矩陣"""
        # 負數表示非對稱
        matrix = [
            [5, 1, 3],
            [2, -1, 2],
            [3, 1, 5]
        ]
        self.assertFalse(is_symmetric_matrix(matrix))

if __name__ == '__main__':
    unittest.main()
