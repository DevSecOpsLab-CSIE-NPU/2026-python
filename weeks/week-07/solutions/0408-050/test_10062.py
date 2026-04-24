import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10062.py 中
# 並且您的解答會提供一個 solve_cows(n, smaller_counts) 函式：
# - n: 乳牛的總數 (int)
# - smaller_counts: 長度為 N-1 的串列，記錄第 2 到第 N 頭牛前面有幾頭較小的牛 (list of ints)
# 回傳格式預期為一個包含 N 個整數的串列 (list of ints)，代表還原後的正確隊伍編號。
from solution_10062 import solve_cows

class TestUVA10062(unittest.TestCase):
    
    def test_general_case(self):
        """
        基礎測試：驗證一般隨機排列的情況。
        輸入 n = 5, smaller_counts = [1, 2, 1, 0]
        - 第 5 頭 (0): 剩餘 [1,2,3,4,5] 的第 1 小，即 1。
        - 第 4 頭 (1): 剩餘 [2,3,4,5] 的第 2 小，即 3。
        - 第 3 頭 (2): 剩餘 [2,4,5] 的第 3 小，即 5。
        - 第 2 頭 (1): 剩餘 [2,4] 的第 2 小，即 4。
        - 第 1 頭 (0): 剩餘 [2] 的第 1 小，即 2。
        故原排列應為 [2, 4, 5, 3, 1]。
        """
        self.assertEqual(solve_cows(5, [1, 2, 1, 0]), [2, 4, 5, 3, 1])

    def test_all_zeros(self):
        """
        極端測試：所有牛前面「都沒有」比自己小的牛。
        代表整個隊伍是完全遞減的狀態，越後面的牛編號越小。
        """
        self.assertEqual(solve_cows(5, [0, 0, 0, 0]), [5, 4, 3, 2, 1])

    def test_increasing(self):
        """
        極端測試：隊伍是完全遞增的狀態 [1, 2, 3, 4, 5]。
        每頭牛前面的所有牛編號都比自己小。
        """
        self.assertEqual(solve_cows(5, [1, 2, 3, 4]), [1, 2, 3, 4, 5])
        
    def test_minimum_cows(self):
        """
        邊界測試：測試題目允許的最小 N 值 (N=2)。
        """
        self.assertEqual(solve_cows(2, [1]), [1, 2])
        self.assertEqual(solve_cows(2, [0]), [2, 1])

if __name__ == '__main__':
    unittest.main()