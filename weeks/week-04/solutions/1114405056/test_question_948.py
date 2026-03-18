"""QUESTION-948 的 Python unittest。"""

from __future__ import annotations

from test_support import DualSolutionTestCase


class TestQuestion948(DualSolutionTestCase):
    """驗證正式版、easy 版、easy-hand 版都符合題目規格。"""

    solution_names = ("question_948.py", "question_948-easy.py", "question_948-easy-hand.py")

    def test_sample_cases(self) -> None:
        sample_input = """2

5 3
2 1 2 3 4
<
1 1 4
=
1 2 5
=

4 2
1 1 2
<
1 3 4
=
"""
        expected_output = """3

0
"""
        self.assert_output_for_all(sample_input, expected_output)

    def test_unweighed_remaining_coin_is_unique_answer(self) -> None:
        test_input = """1

3 1
1 1 2
=
"""
        expected_output = """3
"""
        self.assert_output_for_all(test_input, expected_output)

    def test_single_unbalanced_weighing_is_still_ambiguous(self) -> None:
        test_input = """1

4 1
1 1 2
<
"""
        expected_output = """0
"""
        self.assert_output_for_all(test_input, expected_output)

    def test_genuine_reference_coin_can_remove_ambiguity(self) -> None:
        test_input = """1

4 3
1 1 2
=
1 3 4
<
1 3 1
<
"""
        expected_output = """3
"""
        self.assert_output_for_all(test_input, expected_output)


if __name__ == "__main__":
    import unittest

    unittest.main(verbosity=2)
