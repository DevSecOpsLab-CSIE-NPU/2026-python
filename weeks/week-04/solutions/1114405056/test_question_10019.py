"""QUESTION-10019 的 Python unittest。"""

from __future__ import annotations

import unittest

from test_support import DualSolutionTestCase


class TestQuestion10019(DualSolutionTestCase):
    solution_names = ("question_10019.py", "question_10019-easy.py", "question_10019-easy-hand.py")

    def test_multiple_pairs_until_eof(self) -> None:
        test_input = """10 12
10 14
100 200
"""
        expected_output = """2
4
100
"""
        self.assert_output_for_all(test_input, expected_output)

    def test_large_numbers(self) -> None:
        test_input = """0 9223372036854775808
9223372036854775808 1
"""
        expected_output = """9223372036854775808
9223372036854775807
"""
        self.assert_output_for_all(test_input, expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
