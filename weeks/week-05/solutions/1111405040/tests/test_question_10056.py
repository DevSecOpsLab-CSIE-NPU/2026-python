"""
UVA 10056 測試。
"""

from __future__ import annotations

import unittest

from question_10056 import solve, winning_probability


class TestQuestion10056(unittest.TestCase):
    """測試 What is the Probability?"""

    def test_probability_zero_when_p_is_zero(self) -> None:
        self.assertEqual(winning_probability(3, 0.0, 2), 0.0)

    def test_single_player_eventually_wins(self) -> None:
        self.assertAlmostEqual(winning_probability(1, 0.5, 1), 1.0)

    def test_general_case(self) -> None:
        self.assertAlmostEqual(winning_probability(3, 0.5, 2), 0.2857142857)

    def test_solve_format(self) -> None:
        sample_input = "3\n3 0.0 1\n1 0.5 1\n3 0.5 2\n"
        self.assertEqual(solve(sample_input), "0.0000\n1.0000\n0.2857")


if __name__ == "__main__":
    unittest.main()
