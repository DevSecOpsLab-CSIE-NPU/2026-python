"""測試 UVA 10812 - Beat the Spread!。"""

from __future__ import annotations

import unittest

from test_support import load_module


module = load_module("question-10812.py")


class BeatTheSpreadTest(unittest.TestCase):
    def test_normal_case(self) -> None:
        # 正常情況：可以拆出較大與較小分數。
        self.assertEqual(module.solve_case(40, 20), (30, 10))

    def test_impossible_when_sum_smaller_than_difference(self) -> None:
        # 反例：差大於和，必定無解。
        self.assertIsNone(module.solve_case(20, 40))

    def test_impossible_when_parity_is_odd(self) -> None:
        # 邊界情況：和與差相加為奇數時，無法得到整數解。
        self.assertIsNone(module.solve_case(41, 20))


if __name__ == "__main__":
    unittest.main()
