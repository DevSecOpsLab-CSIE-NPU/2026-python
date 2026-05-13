from __future__ import annotations

import unittest

from question_10929 import describe_number, is_multiple_of_11, solve


class TestQuestion10929(unittest.TestCase):
    def test_multiple_of_11_true_case(self) -> None:
        self.assertTrue(is_multiple_of_11("121"))

    def test_multiple_of_11_false_case(self) -> None:
        self.assertFalse(is_multiple_of_11("123456"))

    def test_multiple_of_11_for_large_value(self) -> None:
        self.assertTrue(is_multiple_of_11("112233445566778899"))

    def test_solve_formats_output(self) -> None:
        sample_input = "121\n123456\n0\n"
        expected = "\n".join(
            [
                "121 is a multiple of 11.",
                "123456 is not a multiple of 11.",
            ]
        )
        self.assertEqual(solve(sample_input), expected)
        self.assertEqual(describe_number("22"), "22 is a multiple of 11.")


if __name__ == "__main__":
    unittest.main()
