"""QUESTION-10038 的 Python unittest。"""

from __future__ import annotations

import unittest

from test_support import DualSolutionTestCase


class TestQuestion10038(DualSolutionTestCase):
    solution_names = ("question_10038.py", "question_10038-easy.py", "question_10038-easy-hand.py")

    def test_sample_cases(self) -> None:
        test_input = """4 1 4 2 3
5 1 4 2 -1 6
"""
        expected_output = """Jolly
Not jolly
"""
        self.assert_output_for_all(test_input, expected_output)

    def test_single_value_and_duplicate_difference(self) -> None:
        test_input = """1 100
4 1 4 7 2
"""
        expected_output = """Jolly
Not jolly
"""
        self.assert_output_for_all(test_input, expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
