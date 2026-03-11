"""
test_q118_hand_typed.py
針對手打程式 q118-Hand-typed.py 的單元測試

由於檔名含連字號無法直接 import，
使用 importlib 動態載入，測試邏輯與 test_q118.py 相同。
"""

import importlib.util
import unittest
from pathlib import Path

# ── 動態載入 q118-Hand-typed.py ──────────────────────────────────────────────
_file = Path(__file__).parent / "q118-Hand-typed.py"
_spec = importlib.util.spec_from_file_location("q118_hand_typed", _file)
_mod  = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

solve = _mod.solve


class TestSolve(unittest.TestCase):
    """完整輸入輸出整合測試（含轉向、移動、掉落、scent 保護）"""

    def test_uva_official_sample(self):
        """UVA 118 官方三組範例，預期輸出完全一致"""
        sample = (
            "5 3\n"
            "1 1 E\n"
            "RFRFRFRF\n"
            "3 2 N\n"
            "FRRFLLFFRRFLL\n"
            "0 3 W\n"
            "LLFFFLFLFL\n"
        )
        expected = "1 1 E\n3 3 N LOST\n2 3 S"
        self.assertEqual(solve(sample), expected)

    def test_single_robot_turn_only(self):
        """只轉向不移動，位置應不變"""
        self.assertEqual(solve("5 3\n2 2 N\nLRLR"), "2 2 N")

    def test_single_robot_walk_to_boundary(self):
        """走到邊界格（不超出），應安全存活"""
        self.assertEqual(solve("5 3\n0 0 N\nFFF"), "0 3 N")

    def test_single_robot_falls_immediately(self):
        """站在邊界直接往外走，應掉落"""
        self.assertEqual(solve("5 3\n0 0 S\nF"), "0 0 S LOST")

    def test_fall_north(self):
        """從北邊掉落"""
        self.assertEqual(solve("5 3\n0 3 N\nF"), "0 3 N LOST")

    def test_fall_east(self):
        """從東邊掉落"""
        self.assertEqual(solve("5 3\n5 0 E\nF"), "5 0 E LOST")

    def test_fall_west(self):
        """從西邊掉落"""
        self.assertEqual(solve("5 3\n0 0 W\nF"), "0 0 W LOST")

    def test_scent_prevents_fall(self):
        """
        機器人 1 在 (0,3) 掉落留下 scent；
        機器人 2 走到 (0,3) 後嘗試 F，應被保護不掉落
        """
        sample = "5 3\n0 3 N\nF\n0 0 N\nFFFRF\n"
        lines = solve(sample).splitlines()
        self.assertEqual(lines[0], "0 3 N LOST")
        self.assertEqual(lines[1], "1 3 E")

    def test_scent_only_blocks_dangerous_f(self):
        """scent 保護後，轉向往安全方向前進仍然有效"""
        sample = "5 3\n0 3 N\nF\n0 3 N\nFRF\n"
        lines = solve(sample).splitlines()
        self.assertEqual(lines[0], "0 3 N LOST")
        self.assertEqual(lines[1], "1 3 E")   # F 被忽略，R 後再 F 往東

    def test_multiple_robots_no_interaction(self):
        """多個機器人往不同方向走，互不干擾"""
        sample = (
            "5 5\n"
            "0 0 E\nFF\n"   # → 2 0 E
            "5 5 W\nFF\n"   # → 3 5 W
            "2 2 N\nFF\n"   # → 2 4 N
        )
        lines = solve(sample).splitlines()
        self.assertEqual(lines[0], "2 0 E")
        self.assertEqual(lines[1], "3 5 W")
        self.assertEqual(lines[2], "2 4 N")

    def test_exact_boundary_safe(self):
        """剛好走到邊界格（x=max_x），應安全存活"""
        self.assertEqual(solve("3 3\n0 0 E\nFFF"), "3 0 E")

    def test_one_over_boundary_lost(self):
        """多走一步超出邊界，應掉落"""
        self.assertEqual(solve("3 3\n0 0 E\nFFFF"), "3 0 E LOST")

    def test_right_turn_sequence(self):
        """右轉四次應回到原方向，且不移動"""
        result = solve("5 5\n3 3 N\nRRRR")
        self.assertEqual(result, "3 3 N")

    def test_left_turn_sequence(self):
        """左轉四次應回到原方向，且不移動"""
        result = solve("5 5\n3 3 S\nLLLL")
        self.assertEqual(result, "3 3 S")


if __name__ == "__main__":
    unittest.main(verbosity=2)
