"""測試 UVA 10908 - Largest Square。"""

from __future__ import annotations

import unittest

from test_support import load_module


module = load_module("question-10908.py")


class LargestSquareTest(unittest.TestCase):
    def test_sample_center(self) -> None:
        # 正常情況：中心點周圍有多層相同字元。
        grid = [
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaccaaaaaa"),
            list("aaccaaaaaa"),
        ]
        self.assertEqual(module.largest_square_side(grid, 1, 2), 3)

    def test_single_cell_grid(self) -> None:
        # 邊界情況：只有一個格子時，答案一定是 1。
        self.assertEqual(module.largest_square_side([list("x")], 0, 0), 1)

    def test_non_symmetric_square_stops_early(self) -> None:
        # 反例：若外圈出現不同字元，就不能再擴張。
        grid = [
            list("aaaaa"),
            list("ababa"),
            list("aaaaa"),
            list("ababa"),
            list("aaaaa"),
        ]
        self.assertEqual(module.largest_square_side(grid, 2, 2), 1)


if __name__ == "__main__":
    unittest.main()
