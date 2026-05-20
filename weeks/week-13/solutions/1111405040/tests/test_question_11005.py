"""
UVA 11005 測試。
"""

from __future__ import annotations

import unittest

from question_11005 import cheapest_bases, cost_in_base, solve
from question_11005_easy import solve as solve_easy


class TestQuestion11005(unittest.TestCase):
    """驗證 Cheapest Base。"""

    def test_cost_in_base_for_zero(self) -> None:
        """0 在任何進位都只會使用數字 0。"""
        costs = list(range(36))
        self.assertEqual(cost_in_base(0, 2, costs), 0)

    def test_cost_in_base_for_normal_number(self) -> None:
        """驗證一般數字的位數成本加總。"""
        costs = [1] * 36
        self.assertEqual(cost_in_base(31, 16, costs), 2)

    def test_cheapest_bases(self) -> None:
        """當所有字元成本都相同時，位數最少的進位最便宜。"""
        costs = [1] * 36
        self.assertEqual(cheapest_bases(5, costs), list(range(6, 37)))

    def test_solve(self) -> None:
        """正式版與 easy 版都要輸出相同答案。"""
        data = "\n".join(
            [
                "1",
                "1 1 1 1 1 1 1 1 1",
                "1 1 1 1 1 1 1 1 1",
                "1 1 1 1 1 1 1 1 1",
                "1 1 1 1 1 1 1 1 1",
                "2",
                "0",
                "5",
            ]
        )
        expected = "\n".join(
            [
                "Case 1:",
                "Cheapest base(s) for number 0: " + " ".join(str(base) for base in range(2, 37)),
                "Cheapest base(s) for number 5: " + " ".join(str(base) for base in range(6, 37)),
            ]
        )
        self.assertEqual(solve(data), expected)
        self.assertEqual(solve_easy(data), expected)


if __name__ == "__main__":
    unittest.main()
