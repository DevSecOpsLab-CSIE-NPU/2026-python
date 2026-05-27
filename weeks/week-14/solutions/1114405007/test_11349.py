"""
題目 11349 - Symmetric Matrix (對稱矩陣判斷) 測試程式
單元測試 (Unit Test) - 驗證解題程式的正確性
"""

import unittest
from solution_11349 import is_symmetric_matrix


class TestSymmetricMatrix(unittest.TestCase):
    """對稱矩陣判斷函數的單元測試類別"""

    def test_symmetric_matrix_3x3(self):
        """測試3x3對稱矩陣"""
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [3, 1, 5]
        ]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_non_symmetric_matrix_3x3(self):
        """測試3x3非對稱矩陣"""
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [0, 1, 5]
        ]
        self.assertFalse(is_symmetric_matrix(matrix))

    def test_symmetric_matrix_1x1(self):
        """測試1x1矩陣（單一元素）"""
        matrix = [[5]]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_symmetric_matrix_2x2(self):
        """測試2x2對稱矩陣"""
        matrix = [
            [1, 2],
            [2, 1]
        ]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_symmetric_matrix_4x4(self):
        """測試4x4對稱矩陣"""
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 6, 5],
            [5, 6, 6, 5],
            [4, 3, 2, 1]
        ]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_negative_number_not_symmetric(self):
        """測試含有負數的矩陣（應判定為非對稱）"""
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [3, 1, -5]  # 負數存在
        ]
        self.assertFalse(is_symmetric_matrix(matrix))

    def test_all_zeros(self):
        """測試全零矩陣（對稱）"""
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertTrue(is_symmetric_matrix(matrix))

    def test_diagonal_matrix(self):
        """測試對角線矩陣（對稱）"""
        matrix = [
            [1, 0, 0],
            [0, 2, 0],
            [0, 0, 1]
        ]
        self.assertTrue(is_symmetric_matrix(matrix))


if __name__ == '__main__':
    unittest.main()
