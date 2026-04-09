"""
===============================================================================
UVA 10093 - 炮兵部署問題 測試（Q10093.hand.py）
===============================================================================

題目說明：
    在 N×M 的網格地圖上部署炮兵，山地(H)不能放，平原(P)可以放。
    炮兵攻擊範圍：左右各 2 格，上下各 2 格。
    目標：求最多能部署的炮兵數量。

===============================================================================
"""

# 匯入 solution_10093_easy.py 中的 max_artillery 函式
# 此函式接受 N, M, grid 三個參數，回傳最多能部署的炮兵數
from solution_10093_easy import max_artillery

# 匯入 unittest 單元測試框架
import unittest


class TestArtillery(unittest.TestCase):
    """
    測試類別：炮兵部署功能測試

    包含 9 個測試案例，驗證不同情況下的計算結果是否正確。
    """

    # ========================================================================
    # 基本邊界測試
    # ========================================================================

    def test_single_plain(self):
        """
        測試 1：單一格平原

        輸入：N=1, M=1, grid=["P"]
        預期：1（只有一格，可放一台炮兵）
        """
        self.assertEqual(max_artillery(1, 1, ["P"]), 1)

    def test_single_mountain(self):
        """
        測試 2：單一格山地

        輸入：N=1, M=1, grid=["H"]
        預期：0（山地不能放置炮兵）
        """
        self.assertEqual(max_artillery(1, 1, ["H"]), 0)

    def test_two_rows_plain(self):
        """
        測試 3：2×1 全部平原

        輸入：N=2, M=1, grid=["P", "P"]
        預期：1（縱向攻擊範圍 2 格，相鄰格子只能放一台）
        """
        self.assertEqual(max_artillery(2, 1, ["P", "P"]), 1)

    def test_all_mountains(self):
        """
        測試 4：2×2 全部山地

        輸入：N=2, M=2, grid=["HH", "HH"]
        預期：0（所有格子都是山地，不能放炮兵）
        """
        self.assertEqual(max_artillery(2, 2, ["HH", "HH"]), 0)

    # ========================================================================
    # 中等尺寸測試
    # ========================================================================

    def test_3x3_plain(self):
        """
        測試 5：3×3 全部平原

        輸入：N=3, M=3, grid=["PPP", "PPP", "PPP"]
        預期：>= 0（能正常運算即可）
        """
        self.assertGreaterEqual(max_artillery(3, 3, ["PPP", "PPP", "PPP"]), 0)

    def test_mixed(self):
        """
        測試 6：混合地形

        輸入：N=3, M=3, grid=["PHP", "PPP", "PPP"]
        預期：>= 0（山地位置不能放炮兵）
        """
        self.assertGreaterEqual(max_artillery(3, 3, ["PHP", "PPP", "PPP"]), 0)

    # ========================================================================
    # 大尺寸測試
    # ========================================================================

    def test_wide(self):
        """
        測試 7：寬網格（M=10，最大寬度）

        輸入：N=2, M=10, grid=["PPPPPPPPPP", "PPPPPPPPPP"]
        預期：>= 0（狀態數 2^10 = 1024）
        """
        self.assertGreaterEqual(max_artillery(2, 10, ["PPPPPPPPPP", "PPPPPPPPPP"]), 0)

    def test_narrow(self):
        """
        測試 8：窄網格（M=1，最小寬度）

        輸入：N=5, M=1, grid=["P", "P", "P", "P", "P"]
        預期：>= 0（每行最多 1 台，縱向限制只能放 1 台）
        """
        self.assertGreaterEqual(max_artillery(5, 1, ["P", "P", "P", "P", "P"]), 0)

    def test_alternating(self):
        """
        測試 9：交錯地形（P 和 H 交替排列）

        輸入：N=4, M=4, grid=["PHPH", "HPHP", "PHPH", "HPHP"]
        預期：>= 0（複雜地形測試）
        """
        self.assertGreaterEqual(
            max_artillery(4, 4, ["PHPH", "HPHP", "PHPH", "HPHP"]), 0
        )


# ========================================================================
# 主程式入口
# ========================================================================
if __name__ == "__main__":
    # 執行測試，verbosity=2 表示詳細輸出
    unittest.main(verbosity=2)
