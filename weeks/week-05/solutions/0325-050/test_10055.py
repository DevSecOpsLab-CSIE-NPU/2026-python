import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10055.py 中
# 並且您的解答會提供一個 solve_functions(n, queries) 函式：
# - n: 函數的數量 (int)
# - queries: 查詢的串列，每個查詢是 tuple，如 (1, i) 或 (2, L, R)
# 回傳所有 v=2 查詢的結果串列 (list of ints，包含 0 或 1)。
from solution_10055 import solve_functions

class TestUVA10055(unittest.TestCase):
    
    def test_all_increasing(self):
        """
        基礎測試：初始狀態下，所有函數都是增函數 (0)。
        不管怎麼查詢區間，結果都應該要是 0。
        """
        n = 5
        queries = [
            (2, 1, 5),
            (2, 2, 4)
        ]
        self.assertEqual(solve_functions(n, queries), [0, 0])

    def test_single_flip(self):
        """
        基礎測試：反轉一個函數的增減性。
        原本是增(0)，反轉後變減(1)。包含它的區間會變成 1，不包含它的區間仍是 0。
        """
        n = 3
        queries = [
            (1, 2),      # 把 f2 反轉為減函數 (1)
            (2, 1, 3),   # 查詢 [1, 3]，包含 f2，所以結果為 1
            (2, 3, 3)    # 查詢 [3, 3]，不包含 f2，所以結果為 0
        ]
        self.assertEqual(solve_functions(n, queries), [1, 0])

    def test_multiple_flips_and_parity(self):
        """
        進階測試：奇偶性與 XOR 邏輯。
        減函數複合減函數會變回增函數 (即 1 + 1 = 0)。
        """
        n = 4
        queries = [
            (1, 1),      # f1 變 1
            (1, 3),      # f3 變 1
            (2, 1, 3),   # [1, 3] 包含兩個 1 (f1, f3)，偶數個，複合為 0
            (2, 1, 2),   # [1, 2] 包含一個 1 (f1)，奇數個，複合為 1
            (1, 3),      # f3 再次反轉，變回 0
            (2, 1, 3)    # 此時 [1, 3] 只有一個 1 (f1)，複合為 1
        ]
        self.assertEqual(solve_functions(n, queries), [0, 1, 1])
        
    def test_edge_case_single_element(self):
        """邊界測試：查詢區間長度只有 1 的情況。"""
        n = 1
        queries = [(1, 1), (2, 1, 1)]
        self.assertEqual(solve_functions(n, queries), [1])

if __name__ == '__main__':
    unittest.main()