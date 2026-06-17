"""
UVA 11150 — 青蛙過獨木橋

測試青蛙跳躍問題的最小踩石子數（動態規劃 + 狀態壓縮）。
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestFrogBridge(unittest.TestCase):
    """測試 UVA 11150：青蛙過獨木橋"""

    def setUp(self):
        try:
            from solution_11150 import min_stones, solve
            self.min_stones = min_stones
            self.solve = solve
        except ImportError:
            self.skipTest("solution_11150.py 尚未撰寫")

    # ─── 基本情況 ───────────────────────────────────

    def test_no_stones(self):
        """橋上無石子 → 最少踩到 0 顆"""
        result = self.min_stones(10, 1, 2, [])
        self.assertEqual(result, 0)

    def test_can_avoid_single_stone_with_s_t(self):
        """S=2, T=3, stone at 3 → 可走 0→2→5 避開"""
        result = self.min_stones(5, 2, 3, [3])
        self.assertEqual(result, 0)

    def test_can_avoid_single_stone(self):
        """可跳過該石子 → 0 顆"""
        # L=5, S=2, T=3, stone at 2
        # 路徑：0→3→5，跳過 2
        result = self.min_stones(5, 2, 3, [2])
        self.assertEqual(result, 0)

    def test_small_bridge_no_stones(self):
        """短橋無石子"""
        result = self.min_stones(1, 1, 1, [])
        self.assertEqual(result, 0)

    # ─── 邊界情況 ───────────────────────────────────

    def test_large_L_no_stones(self):
        """長橋無石子 → 0"""
        result = self.min_stones(10**9, 1, 10, [])
        self.assertEqual(result, 0)

    def test_single_jump_distance(self):
        """S=T=1，只能一步一步跳，所有石子都踩到"""
        result = self.min_stones(5, 1, 1, [1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_stones(self):
        """最多 100 顆石子"""
        stones = list(range(1, 101))
        result = self.min_stones(200, 1, 10, stones)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 100)

    # ─── 整合測試 ───────────────────────────────────

    def test_sample_input(self):
        """範例測試"""
        output = self.solve("10\n2 3 1\n3\n")
        self.assertEqual(output.strip(), "0")


if __name__ == '__main__':
    unittest.main()
