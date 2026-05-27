"""
問題：UVA 11349 — Symmetric Matrix（對稱矩陣）
題目來源：https://zerojudge.tw/ShowProblem?problemid=e513

題意摘要：
給定一個 n×n 的方陣，判斷它是否為「對稱矩陣」。
本題的「對稱」定義為：
  1. 矩陣所有元素均為非負數（>= 0）
  2. 矩陣關於中心點對稱，即 M[i][j] = M[n+1-i][n+1-j]
     （注意是「中心對稱」，不是一般的轉置對稱）
"""

import unittest

# 從解題程式中匯入被測試的函式
from p11349 import is_symmetric


class TestSymmetricMatrix(unittest.TestCase):
    """UVA 11349 對稱矩陣的單元測試"""

    def test_symmetric_3x3(self):
        """測試題目給定的 3x3 對稱矩陣範例"""
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [3, 1, 5],
        ]
        self.assertTrue(is_symmetric(matrix))

    def test_non_symmetric_3x3(self):
        """測試題目給定的 3x3 非對稱矩陣範例"""
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [0, 1, 5],
        ]
        self.assertFalse(is_symmetric(matrix))

    def test_symmetric_1x1(self):
        """測試最小的 1x1 矩陣（單一元素）"""
        matrix = [[5]]
        self.assertTrue(is_symmetric(matrix))

    def test_symmetric_2x2(self):
        """測試 2x2 對稱矩陣"""
        matrix = [
            [1, 2],
            [2, 1],
        ]
        self.assertTrue(is_symmetric(matrix))

    def test_non_symmetric_2x2(self):
        """測試 2x2 非對稱矩陣"""
        matrix = [
            [1, 2],
            [3, 4],
        ]
        self.assertFalse(is_symmetric(matrix))

    def test_negative_element(self):
        """測試含有負數元素的矩陣（應為非對稱）"""
        matrix = [
            [1, -2],
            [-2, 1],
        ]
        self.assertFalse(is_symmetric(matrix))

    def test_symmetric_4x4(self):
        """測試 4x4 中心對稱矩陣"""
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 6, 5],
            [5, 6, 6, 5],
            [4, 3, 2, 1],
        ]
        self.assertTrue(is_symmetric(matrix))

    def test_all_zero_matrix(self):
        """測試全為 0 的矩陣（應為對稱）"""
        matrix = [
            [0, 0],
            [0, 0],
        ]
        self.assertTrue(is_symmetric(matrix))


if __name__ == "__main__":
    unittest.main()
