"""
UVA 11321 — 茵可的陷阱路徑

測試在 N×M 柏油路上放置陷阱，是否會導致道路封死（無路可到終點）。
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestTrapPath(unittest.TestCase):
    """測試 UVA 11321：陷阱放置可行性"""

    def setUp(self):
        try:
            from solution_11321 import can_place, solve
            self.can_place = can_place
            self.solve = solve
        except ImportError:
            self.skipTest("solution_11321.py 尚未撰寫")

    # ─── 基本可放測試 ───────────────────────────────

    def test_empty_grid_single_trap_ok(self):
        """1×1 網格，起點=終點，無陷阱 → 可放（但起點列不可放會擋住）"""
        # 起點在左側 y=0，終點在右側 y=M-1=0，即起點=終點
        # 放在 (0,0) 會擋住唯一的路，所以不可放
        result = self.can_place(1, 1, [(0, 0)])
        self.assertEqual(result, [False])

    def test_2x2_place_center_ok(self):
        """2×2 網格，放 (0,1) 仍有其他路徑"""
        result = self.can_place(2, 2, [(0, 1)])
        self.assertEqual(result, [True])

    def test_2x2_block_all(self):
        """2×2 網格，試圖阻塞所有路徑"""
        # N=2, M=2, 放 (0,0) 和 (1,0)（左側全部封死）
        result = self.can_place(2, 2, [(0, 0), (1, 0)])
        self.assertEqual(result, [True, False])

    # ─── 順序測試（後續陷阱依賴之前已放的陷阱）─────

    def test_sequential_block(self):
        """依序放置，第二個陷阱導致無路時應拒絕"""
        # 3×3 網格
        # 先放 (0,0), (2,0), (0,1), (2,1) — 上下兩排封住，中間仍可走
        traps = [(0, 0), (2, 0), (0, 1), (2, 1)]
        result = self.can_place(3, 3, traps)
        # 最後封 (1,0) 會完全阻塞
        result2 = self.can_place(3, 3, traps + [(1, 0)])
        self.assertEqual(result2[-1], False)

    # ─── 邊界情況 ───────────────────────────────────

    def test_large_grid_no_block(self):
        """大網格放少量陷阱，應全部可放"""
        traps = [(0, 0), (5, 5), (9, 9)]
        result = self.can_place(10, 10, traps)
        self.assertEqual(result, [True, True, True])

    def test_single_row(self):
        """1×M 單行，只能從左走到右"""
        # N=1, M=5
        # 放在 (0,4) 是最後一列（終點），必須踩到才能過→不可放
        result = self.can_place(1, 5, [(0, 4)])
        self.assertEqual(result, [False])
        result2 = self.can_place(1, 5, [(0, 2)])
        self.assertEqual(result2, [False])

    # ─── 格式測試 ───────────────────────────────────

    def test_output_format(self):
        """檢查輸出格式"""
        output = self.solve("3 3 2\n0 0\n0 1\n")
        lines = [l.strip() for l in output.strip().splitlines() if l]
        self.assertEqual(len(lines), 2)
        for line in lines:
            self.assertIn(line, ["<(_ _)>", ">_<"])


if __name__ == '__main__':
    unittest.main()
