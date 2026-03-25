# weeks/week-04/solutions/MidSummerDream.py
import unittest

class DreamSolver:
    """解決仲夏夜之夢中位數問題"""
    
    @staticmethod
    def solve(numbers):
        """
        傳入數字列表，回傳 (最小中位數, 輸入中符合個數, 整數可能個數)
        """
        n = len(numbers)
        numbers.sort()
        
        # 關鍵 index：(n-1)//2 是左中位數，n//2 是右中位數
        mid1 = numbers[(n - 1) // 2]
        mid2 = numbers[n // 2]
        
        # 1. 最小的中位數
        min_median = mid1
        
        # 2. 統計輸入中有多少數字落在 [mid1, mid2] 區間
        count_in_input = 0
        for x in numbers:
            if mid1 <= x <= mid2:
                count_in_input += 1
                
        # 3. 共有多少個整數可以當作 A (區間內的整數數量)
        possible_integers = mid2 - mid1 + 1
        
        return min_median, count_in_input, possible_integers

# --- 單元測試 ---
class TestDream(unittest.TestCase):
    def test_odd_elements(self):
        """測試奇數個元素的情況"""
        solver = DreamSolver()
        # 排序後 [10, 10]，中位數是 10
        self.assertEqual(solver.solve([10, 10]), (10, 2, 1))

    def test_even_elements(self):
        """測試偶數個元素且中位數不同的情況"""
        solver = DreamSolver()
        # 排序後 [1, 2, 3, 4]，左中位 2, 右中位 3
        # 區間 [2, 3]，輸入中有 2, 3 兩數，整數有 2, 3 兩個
        self.assertEqual(solver.solve([1, 2, 3, 4]), (2, 2, 2))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)