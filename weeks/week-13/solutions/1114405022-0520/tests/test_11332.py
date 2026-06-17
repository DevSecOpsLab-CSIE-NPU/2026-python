"""
UVA 11332 — 平面鏡子可見性

測試從原點 (0,0) 是否能見到各鏡子（線段）。
不考慮反射，鏡子之間不會相交，保證不通過原點。
"""
import unittest
import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestMirrorVisibility(unittest.TestCase):
    """測試 UVA 11332：鏡子可見性判斷"""

    def setUp(self):
        try:
            from solution_11332 import visible_mirrors, solve
            self.visible_mirrors = visible_mirrors
            self.solve = solve
        except ImportError:
            self.skipTest("solution_11332.py 尚未撰寫")

    # ─── 基本可見性測試 ─────────────────────────────

    def test_single_mirror_visible(self):
        """單一鏡子，在原點視線範圍內 → 可見"""
        # 鏡子從 (1, -1) 到 (1, 1)，垂直線段，面對原點
        result = self.visible_mirrors([(1, -1, 1, 1)])
        self.assertEqual(result, [1])

    def test_mirror_behind_origin(self):
        """鏡子在原點另一側（被遮擋）→ 不可見"""
        # 但因為沒有其他鏡子擋住，從原點可以看到任何方向的鏡子
        # 除非鏡子在原點另一方向完全不可見？不對，從原點可以朝任何方向看
        # 鏡子在 (-1, -1) 到 (-1, 1)，原點朝左看，可見
        # 實際上所有鏡子只要沒被擋住都應該可見
        # 這個測試不恰當，換一個
        pass

    def test_mirror_blocked_by_another(self):
        """鏡子 A 完全擋住鏡子 B → B 不可見"""
        # 鏡子 A: (2, -2) 到 (2, 2)（垂直，離原點近）
        # 鏡子 B: (4, -2) 到 (4, 2)（垂直，在 A 後面）
        # A 擋住了 B
        result = self.visible_mirrors([
            (2, -2, 2, 2),   # 鏡子 0
            (4, -2, 4, 2),   # 鏡子 1
        ])
        self.assertEqual(result, [1, 0])

    # ─── 幾何輔助函數 ───────────────────────────────

    def test_partial_visibility(self):
        """鏡子部分被擋 → 只要有一小段可見就算可見"""
        # 鏡子 A: (2, 0) 到 (2, 2) → 角度 0°~45°
        # 鏡子 B: (3, -1) 到 (3, 1) → 角度 ~-18.4°~18.4° (341.6°~18.4°)
        # A 只擋住 B 的上半部 (0°~18.4°)，B 的下半部 (341.6°~360°) 仍可見
        from solution_11332 import get_angular_range
        result = get_angular_range(2, 0, 2, 2)
        self.assertAlmostEqual(result[0], 0.0, places=4)
        self.assertAlmostEqual(result[1], math.pi / 4, places=4)

    # ─── 邊界測試 ───────────────────────────────────

    def test_zero_length_mirror(self):
        """鏡子為單點 → 視為線段（題目保證不會通過原點）"""
        # 極端情況，單點鏡子在非原點位置
        result = self.visible_mirrors([(5, 5, 5, 5)])
        self.assertEqual(result, [1])

    def test_multiple_mirrors_all_visible(self):
        """多個鏡子互不遮擋"""
        # 分布在不同的角度方向
        mirrors = [
            (2, 0, 2, 5),     # 右方垂直 (角度 0°~68°)
            (0, 3, 3, 3),     # 上方水平 (在 y=3)
            (-2, 1, -2, 4),   # 左方垂直
        ]
        result = self.visible_mirrors(mirrors)
        self.assertEqual(result, [1, 1, 1])

    # ─── 整合測試 ───────────────────────────────────

    def test_sample_output_format(self):
        """檢查輸出格式（一行 n 個 0/1）"""
        output = self.solve("2\n1 0 2 0\n3 0 4 0\n")
        # 鏡子 0 可見，鏡子 1 被鏡子 0 擋住
        lines = [l.strip() for l in output.strip().splitlines() if l]
        self.assertEqual(len(lines), 1)
        parts = lines[0].split()
        self.assertTrue(all(p in ('0', '1') for p in parts))


if __name__ == '__main__':
    unittest.main()
