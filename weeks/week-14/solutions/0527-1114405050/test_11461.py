import unittest
import math

# ==========================================
# 核心解題邏輯 (可移至獨立檔案例如 solution_11461.py)
# ==========================================
def count_square_numbers(a: int, b: int) -> int:
    """
    計算閉區間 [a, b] 中完全平方數的個數。
    利用數學方法：
    區間內的完全平方數個數等於 floor(sqrt(b)) - ceil(sqrt(a)) + 1
    """
    if a > b or a <= 0:
        return 0
    
    # 計算 a 的平方根，無條件進位 (找到 >= a 的最小完全平方數的根)
    lower_bound = math.ceil(math.sqrt(a))
    # 計算 b 的平方根，無條件捨去 (找到 <= b 的最大完全平方數的根)
    upper_bound = math.floor(math.sqrt(b))
    
    # 若 lower_bound > upper_bound，代表區間內沒有任何完全平方數
    if lower_bound > upper_bound:
        return 0
        
    return upper_bound - lower_bound + 1

# ==========================================
# 單元測試區塊
# ==========================================
class TestSquareNumbers(unittest.TestCase):
    
    def test_case_1(self):
        """測試區間 [1, 4]"""
        self.assertEqual(count_square_numbers(1, 4), 2, "區間 [1, 4] 的輸出應為 2")

    def test_case_2(self):
        """測試區間 [1, 10]"""
        self.assertEqual(count_square_numbers(1, 10), 3, "區間 [1, 10] 的輸出應為 3")
        
    def test_case_3(self):
        """測試區間 [1, 100000]"""
        self.assertEqual(count_square_numbers(1, 100000), 316, "區間 [1, 100000] 的輸出應為 316")

    def test_case_no_squares(self):
        """測試區間內沒有完全平方數的情況，例如 [2, 3]"""
        self.assertEqual(count_square_numbers(2, 3), 0, "區間 [2, 3] 內無完全平方數，應輸出 0")

    def test_case_same_square(self):
        """測試區間起點和終點是同一個完全平方數，例如 [4, 4]"""
        self.assertEqual(count_square_numbers(4, 4), 1, "區間 [4, 4] 的輸出應為 1")
        
if __name__ == '__main__':
    unittest.main()