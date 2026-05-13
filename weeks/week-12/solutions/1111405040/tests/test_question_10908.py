from __future__ import annotations

import unittest

from question_10908 import largest_square, solve


class TestQuestion10908(unittest.TestCase):
    def setUp(self) -> None:
        self.grid = [
            "abbbaaaaaa",
            "abbbaaaaaa",
            "abbbaaaaaa",
            "aaaaaaaaaa",
            "aaaaaaaaaa",
            "aaccaaaaaa",
            "aaccaaaaaa",
        ]

    def test_largest_square_returns_three_for_sample_center(self) -> None:
        self.assertEqual(largest_square(self.grid, 1, 2), 3)

    def test_largest_square_returns_five_for_wider_area(self) -> None:
        self.assertEqual(largest_square(self.grid, 4, 6), 5)

    def test_largest_square_returns_one_on_edge(self) -> None:
        self.assertEqual(largest_square(self.grid, 5, 2), 1)

    def test_solve_sample_case(self) -> None:
        sample_input = "\n".join(
            [
                "1",
                "7 10 4",
                "abbbaaaaaa",
                "abbbaaaaaa",
                "abbbaaaaaa",
                "aaaaaaaaaa",
                "aaaaaaaaaa",
                "aaccaaaaaa",
                "aaccaaaaaa",
                "1 2",
                "2 4",
                "4 6",
                "5 2",
            ]
        )
        expected = "\n".join(["7 10 4", "3", "1", "5", "1"])
        self.assertEqual(solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
