"""
UVA 118 測試。
"""

from __future__ import annotations

import unittest

from question_118 import simulate_robot, solve


class TestSimulation(unittest.TestCase):
    """機器人模擬單元測試。"""

    def test_robot_lost_and_scent(self) -> None:
        scents: set[tuple[int, int]] = set()

        first = simulate_robot(
            max_x=1,
            max_y=1,
            scents=scents,
            start_x=0,
            start_y=0,
            start_direction="S",
            commands="F",
        )
        self.assertEqual(first, (0, 0, "S", True))
        self.assertIn((0, 0), scents)

        second = simulate_robot(
            max_x=1,
            max_y=1,
            scents=scents,
            start_x=0,
            start_y=0,
            start_direction="S",
            commands="F",
        )
        self.assertEqual(second, (0, 0, "S", False))


class TestSolve(unittest.TestCase):
    """端對端解題測試。"""

    def test_uva_sample(self) -> None:
        text = "\n".join(
            [
                "5 3",
                "1 1 E",
                "RFRFRFRF",
                "3 2 N",
                "FRRFLLFFRRFLL",
                "0 3 W",
                "LLFFFLFLFL",
            ]
        )
        expected = "\n".join(
            [
                "1 1 E",
                "3 3 N LOST",
                "2 3 S",
            ]
        )
        self.assertEqual(solve(text), expected)

    def test_scent_prevents_second_loss(self) -> None:
        text = "\n".join(
            [
                "1 1",
                "0 0 S",
                "F",
                "0 0 S",
                "F",
            ]
        )
        expected = "\n".join(
            [
                "0 0 S LOST",
                "0 0 S",
            ]
        )
        self.assertEqual(solve(text), expected)


if __name__ == "__main__":
    unittest.main()
