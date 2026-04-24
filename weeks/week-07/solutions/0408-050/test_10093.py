import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10093.py 中
# 並且您的解答會提供一個 solve_artillery(n, m, grid) 函式：
# - n: 網格的列數 (int)
# - m: 網格的行數 (int)
# - grid: 包含 N 個字串的串列，每個字串長度為 M，代表地形 ('P' 或 'H')
# 回傳最多能部署的炮兵部隊數量 (int)。
from solution_10093 import solve_artillery

class TestUVA10093(unittest.TestCase):
    
    def test_classic_example(self):
        """
        經典範例測試：
        這是一組最常被用來驗證炮兵部隊問題的測資。
        N = 5, M = 4
        地形如下，最佳解是佈署 6 支炮兵部隊。
        """
        grid = [
            "PHPP",
            "PPHH",
            "PPPP",
            "PHPP",
            "PHHP"
        ]
        self.assertEqual(solve_artillery(5, 4, grid), 6)

    def test_all_mountains(self):
        """
        邊界測試：全是山地 (H)。
        因為炮兵只能佈署在平原 (P) 上，所以預期輸出為 0。
        這能測試程式是否正確處理了地形遮罩 (Mountain Mask)。
        """
        grid = [
            "HHHH",
            "HHHH"
        ]
        self.assertEqual(solve_artillery(2, 4, grid), 0)

    def test_single_row_plains(self):
        """
        基礎測試：只有單列且全是平原 (P)。
        M = 10，因為左右攻擊範圍各為 2 格，所以最密集的佈署方式是每隔 2 格放一個
        (放置在索引 0, 3, 6, 9)，共可佈署 4 個炮兵。
        這能測試單行內部狀態 (左右不互相攻擊) 的合法性檢查是否正確。
        """
        grid = ["PPPPPPPPPP"]
        self.assertEqual(solve_artillery(1, 10, grid), 4)

if __name__ == '__main__':
    unittest.main()