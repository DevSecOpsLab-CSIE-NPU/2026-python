"""QUESTION-10008 的 Python unittest。"""

from __future__ import annotations

import unittest

from test_support import DualSolutionTestCase


class TestQuestion10008(DualSolutionTestCase):
    solution_names = ("question_10008.py", "question_10008-easy.py", "question_10008-easy-hand.py")

    def test_sort_by_frequency_then_letter(self) -> None:
        test_input = """5
AaBb
CCcc
bB
123!!
zZz
"""
        expected_output = """B 4
C 4
Z 3
A 2
"""
        self.assert_output_for_all(test_input, expected_output)

    def test_ignore_non_letters_and_merge_cases(self) -> None:
        test_input = """3
abc

A a
"""
        expected_output = """A 3
B 1
C 1
"""
        self.assert_output_for_all(test_input, expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
