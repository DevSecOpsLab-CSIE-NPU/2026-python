import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_299.py 中
# 並且您的解答會提供一個 count_swaps(carriages) 函式：
# 它接收一個包含車廂編號的串列 (list of ints)，並回傳最少需要相鄰交換的次數 (int)。
from solution_299 import count_swaps

class TestUVA299(unittest.TestCase):
    
    def test_sample_case(self):
        """
        測試基礎的車廂排列情況。
        例如 [1, 3, 2] 只需要將 3 和 2 交換 1 次即可排序完成 ([1, 2, 3])。
        """
        self.assertEqual(count_swaps([1, 3, 2]), 1)
        
        # 另一個常見範例，[4, 3, 2, 1] 需要完全反轉，也就是 3 + 2 + 1 = 6 次交換
        self.assertEqual(count_swaps([4, 3, 2, 1]), 6)

    def test_already_sorted(self):
        """
        基礎測試：測試已經排好序的車廂。
        預期不需要任何交換，回傳 0。
        """
        self.assertEqual(count_swaps([1, 2, 3, 4, 5]), 0)

    def test_edge_cases(self):
        """
        邊界情況測試：
        當車廂數量為 0 或 1 的時候，排序已經完成，永遠不需要交換。
        """
        self.assertEqual(count_swaps([]), 0)
        self.assertEqual(count_swaps([1]), 0)
        self.assertEqual(count_swaps([2]), 0)

    def test_worst_case(self):
        """
        效能與極端值測試：
        測試題目給定的最大車廂數量 L=50 的最壞情況 (完全逆序排列)。
        50 個元素的完全逆序需要 (50 * 49) / 2 = 1225 次交換。
        """
        worst_case_train = list(range(50, 0, -1))  # [50, 49, 48, ..., 1]
        self.assertEqual(count_swaps(worst_case_train), 1225)

if __name__ == '__main__':
    unittest.main()