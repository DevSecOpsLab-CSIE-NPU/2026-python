from __future__ import annotations

import unittest

from question_10922 import describe_number, nine_degree, solve


class TestQuestion10922(unittest.TestCase):
    def test_nine_degree_for_single_nine(self) -> None:
        self.assertEqual(nine_degree("9"), 1)

    def test_nine_degree_for_repeated_nines(self) -> None:
        self.assertEqual(nine_degree("999999999"), 2)

    def test_nine_degree_returns_none_for_non_multiple(self) -> None:
        self.assertIsNone(nine_degree("12345"))

    def test_solve_formats_output(self) -> None:
        sample_input = "999999999\n12345\n0\n"
        expected = "\n".join(
            [
                "999999999 is a multiple of 9 and has 9-degree 2.",
                "12345 is not a multiple of 9.",
            ]
        )
        self.assertEqual(solve(sample_input), expected)
        self.assertEqual(
            describe_number("9"),
            "9 is a multiple of 9 and has 9-degree 1.",
        )


if __name__ == "__main__":
    unittest.main()
