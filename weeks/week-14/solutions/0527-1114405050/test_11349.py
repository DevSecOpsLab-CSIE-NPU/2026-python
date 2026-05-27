import unittest

# ==========================================
# 核心解題邏輯 (可移至獨立檔案例如 solution_11349.py)
# ==========================================
def is_symmetric(n: int, matrix: list[list[int]]) -> bool:
    """
    判斷給定的 n x n 矩陣是否為「中心對稱矩陣」。
    條件 1: 矩陣中所有元素必須 >= 0
    條件 2: 關於中心點對稱，即 matrix[i][j] == matrix[n-1-i][n-1-j]
    """
    for i in range(n):
        for j in range(n):
            # 條件 1: 若遇到負數，則不可能是對稱矩陣
            if matrix[i][j] < 0:
                return False
            
            # 條件 2: 檢查是否與中心對稱位置的值相等
            # 0-based 索引中，對稱位置為 (n - 1 - i, n - 1 - j)
            if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                return False
                
    return True

# ==========================================
# 單元測試區塊
# ==========================================
class TestSymmetricMatrix(unittest.TestCase):
    
    def test_symmetric_case(self):
        """測試正常的對稱矩陣 (符合所有條件)"""
        n = 3
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [3, 1, 5]
        ]
        self.assertTrue(is_symmetric(n, matrix), "應該判定為對稱矩陣")

    def test_non_symmetric_case(self):
        """測試非對稱矩陣 (元素皆為正數，但未中心對稱)"""
        n = 3
        matrix = [
            [5, 1, 3],
            [2, 0, 2],
            [0, 1, 5] # 左下角為 0，與右上角 3 不匹配
        ]
        self.assertFalse(is_symmetric(n, matrix), "應該判定為非對稱矩陣")

    def test_negative_number_case(self):
        """測試包含負數的矩陣 (即使數值中心對稱，只要有負數即為非對稱)"""
        n = 3
        matrix = [
            [5, 1, -3],
            [2, 0, 2],
            [-3, 1, 5]
        ]
        self.assertFalse(is_symmetric(n, matrix), "含有負數，應判定為非對稱矩陣")
        
    def test_single_element(self):
        """測試邊界情況：1x1 的矩陣"""
        self.assertTrue(is_symmetric(1, [[5]]), "1x1 正數矩陣應為對稱")
        self.assertFalse(is_symmetric(1, [[-5]]), "1x1 負數矩陣應為非對稱")

if __name__ == '__main__':
    unittest.main()