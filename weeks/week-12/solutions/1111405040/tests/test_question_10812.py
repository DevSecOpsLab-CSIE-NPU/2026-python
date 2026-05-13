from __future__ import annotations

import unittest

from question_10812 import find_scores, solve


class TestQuestion10812(unittest.TestCase):
    def test_find_scores_valid_case(self) -> None:
        self.assertEqual(find_scores(40, 20), (30, 10))

    def test_find_scores_impossible_when_diff_larger_than_total(self) -> None:
        self.assertIsNone(find_scores(20, 40))

    def test_find_scores_impossible_when_parity_mismatch(self) -> None:
        self.assertIsNone(find_scores(41, 20))

    def test_solve_multiple_cases(self) -> None:
        sample_input = "3\n40 20\n20 40\n41 21\n"
        expected = "30 10\nimpossible\n31 10"
        self.assertEqual(solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
