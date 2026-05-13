from __future__ import annotations

import unittest

from question_10931 import parity_text, solve


class TestQuestion10931(unittest.TestCase):
    def test_parity_text_for_one(self) -> None:
        self.assertEqual(parity_text(1), "The parity of 1 is 1 (mod 2).")

    def test_parity_text_for_twenty_one(self) -> None:
        self.assertEqual(parity_text(21), "The parity of 10101 is 3 (mod 2).")

    def test_parity_text_for_large_value(self) -> None:
        self.assertEqual(parity_text(31), "The parity of 11111 is 5 (mod 2).")

    def test_solve_multiple_lines(self) -> None:
        sample_input = "1\n2\n10\n21\n0\n"
        expected = "\n".join(
            [
                "The parity of 1 is 1 (mod 2).",
                "The parity of 10 is 1 (mod 2).",
                "The parity of 1010 is 2 (mod 2).",
                "The parity of 10101 is 3 (mod 2).",
            ]
        )
        self.assertEqual(solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
