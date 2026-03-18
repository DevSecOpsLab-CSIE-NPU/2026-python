"""QUESTION-10035 的 Python unittest。"""

from __future__ import annotations

import unittest

from test_support import DualSolutionTestCase


class TestQuestion10035(DualSolutionTestCase):
    solution_names = ("question_10035.py", "question_10035-easy.py", "question_10035-easy-hand.py")

    def test_sample_cases(self) -> None:
        test_input = """123 456
555 555
123 594
0 0
"""
        expected_output = """No carry operation.
3 carry operations.
1 carry operation.
"""
        self.assert_output_for_all(test_input, expected_output)

    def test_long_carry_chain(self) -> None:
        test_input = """1 99999
999 1
0 0
"""
        expected_output = """5 carry operations.
3 carry operations.
"""
        self.assert_output_for_all(test_input, expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
