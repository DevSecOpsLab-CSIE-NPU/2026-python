import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10057.py 中
# 並且您的解答會提供一個 solve_password(numbers) 函式：
# 接收一個包含所有輸入數字的整數串列 (不包含開頭的數量 n)
# 回傳一個包含三個整數的 tuple：(最小的最佳 A, 陣列中等於最佳 A 的元素個數, 有多少個可能的最佳 A)
from solution_10057 import solve_password

class TestUVA10057(unittest.TestCase):
    
    def test_odd_elements(self):
        """
        基礎測試 1：奇數個元素。
        輸入：[2, 4, 6]
        最佳 A 必定是最中間的數字 (4)。
        陣列中等於 4 的有 1 個。
        可能的 A 只有 1 種 (4)。
        預期輸出：(4, 1, 1)
        """
        self.assertEqual(solve_password([2, 4, 6]), (4, 1, 1))

    def test_even_elements_distinct_medians(self):
        """
        基礎測試 2：偶數個元素，且中間兩個數字不同。
        輸入：[1, 2, 4, 5]
        中間兩個數字是 2 和 4，任何介於 [2, 4] 的整數都是最佳 A (2, 3, 4)。
        最小的 A 是 2。
        輸入陣列中落在 [2, 4] 範圍內的數字有 2 和 4，共 2 個。
        可能的整數 A 有 2, 3, 4，共 3 個。
        預期輸出：(2, 2, 3)
        """
        self.assertEqual(solve_password([1, 2, 4, 5]), (2, 2, 3))

    def test_even_elements_same_medians(self):
        """
        陷阱測試：偶數個元素，但中間兩個數字相同。
        輸入：[2, 4, 4, 6]
        中間兩個數字都是 4，最佳 A 範圍是 [4, 4]。
        最小的 A 是 4。
        輸入陣列中落在 [4, 4] 範圍內的數字有兩個 4，共 2 個。
        可能的整數 A 只有 4，共 1 種。
        預期輸出：(4, 2, 1)
        """
        self.assertEqual(solve_password([2, 4, 4, 6]), (4, 2, 1))

    def test_unsorted_elements(self):
        """
        進階測試：未排序的輸入。
        輸入：[10, 1, 3, 2] -> 排序後 [1, 2, 3, 10]
        中間兩個是 2 和 3。
        最小 A 是 2。
        陣列中落在 [2, 3] 內的有 2 和 3，共 2 個。
        可能 A 有 2, 3，共 2 種。
        預期輸出：(2, 2, 2)
        """
        self.assertEqual(solve_password([10, 1, 3, 2]), (2, 2, 2))

if __name__ == '__main__':
    unittest.main()