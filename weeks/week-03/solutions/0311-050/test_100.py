import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_100.py 中
# 並且您的解答會提供兩個主要函式：
# 1. get_cycle_length(n): 計算單一數字 n 的 cycle-length
# 2. solve(i, j): 計算 i 到 j 區間內的最大 cycle-length，並回傳 (i, j, max_length)
from solution_100 import get_cycle_length, solve

class TestUVA100(unittest.TestCase):
    
    def test_get_cycle_length(self):
        """
        測試單一整數 n 的 cycle-length 運算是否正確
        """
        # n = 1 時，數列只有 1，所以長度為 1
        self.assertEqual(get_cycle_length(1), 1)
        # 根據題目範例，n = 22 的數列長度為 16
        self.assertEqual(get_cycle_length(22), 16)

    def test_solve_normal_order(self):
        """
        測試題目給定的測資 (正常的 i <= j 情況)
        """
        # solve 函式預期會回傳一個包含三個元素的 Tuple：(原始 i, 原始 j, 區間內的最大 cycle-length)
        self.assertEqual(solve(1, 10), (1, 10, 20))
        self.assertEqual(solve(100, 200), (100, 200, 125))
        self.assertEqual(solve(201, 210), (201, 210, 89))
        self.assertEqual(solve(900, 1000), (900, 1000, 174))

    def test_solve_reversed_order(self):
        """
        測試當 i > j 時的邊界情況（UVA 100 的經典陷阱）
        雖然計算區間必須是 [j, i]，但輸出的前兩個數字必須維持原始輸入的順序 (i, j)
        """
        self.assertEqual(solve(10, 1), (10, 1, 20))

if __name__ == '__main__':
    unittest.main()