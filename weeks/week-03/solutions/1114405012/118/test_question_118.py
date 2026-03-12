"""
question_118.py 的單元測試

測試重點：
1. 方向旋轉（L/R）
2. 前進與邊界判斷
3. scent 規則（避免重複掉落）
4. 官方樣例整體輸入輸出

所有註解採用繁體中文。
"""

import unittest

from question_118 import (
    turn_left,
    turn_right,
    is_outside,
    simulate_robot,
    solve_text,
)


class TestTurn(unittest.TestCase):
    """測試轉向函式。"""

    def test_turn_left(self):
        self.assertEqual(turn_left("N"), "W")
        self.assertEqual(turn_left("W"), "S")

    def test_turn_right(self):
        self.assertEqual(turn_right("N"), "E")
        self.assertEqual(turn_right("W"), "N")


class TestBoundary(unittest.TestCase):
    """測試邊界判斷。"""

    def test_inside(self):
        self.assertFalse(is_outside(0, 0, 5, 3))
        self.assertFalse(is_outside(5, 3, 5, 3))

    def test_outside(self):
        self.assertTrue(is_outside(-1, 0, 5, 3))
        self.assertTrue(is_outside(0, 4, 5, 3))


class TestRobotSimulation(unittest.TestCase):
    """測試單機器人模擬。"""

    def test_not_lost(self):
        scents = set()
        x, y, d, lost = simulate_robot(1, 1, "E", "RFRFRFRF", 5, 3, scents)
        self.assertEqual((x, y, d, lost), (1, 1, "E", False))

    def test_lost_and_leave_scent(self):
        scents = set()
        x, y, d, lost = simulate_robot(3, 2, "N", "FRRFLLFFRRFLL", 5, 3, scents)
        self.assertEqual((x, y, d, lost), (3, 3, "N", True))
        self.assertIn((3, 3), scents)

    def test_scent_prevents_second_loss(self):
        scents = {(3, 3)}
        # 同樣在 (3,3) 朝北前進會掉落，但因有 scent 應忽略該 F
        x, y, d, lost = simulate_robot(3, 3, "N", "F", 5, 3, scents)
        self.assertEqual((x, y, d, lost), (3, 3, "N", False))


class TestSolveText(unittest.TestCase):
    """測試整份輸入輸出。"""

    def test_uva_sample(self):
        raw = "\n".join([
            "5 3",
            "1 1 E",
            "RFRFRFRF",
            "3 2 N",
            "FRRFLLFFRRFLL",
            "0 3 W",
            "LLFFFLFLFL",
            "",
        ])

        expected = "\n".join([
            "1 1 E",
            "3 3 N LOST",
            "2 3 S",
        ])

        self.assertEqual(solve_text(raw), expected)

    def test_empty_input(self):
        self.assertEqual(solve_text("\n\n"), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
