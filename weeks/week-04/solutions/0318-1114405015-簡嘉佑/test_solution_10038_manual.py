"""
UVA 10038 - Jolly Jumpers
Unit tests for solution_10038_manual.py
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_10038_manual import is_jolly_sequence, judge_line


class TestJollyJumpers10038Manual(unittest.TestCase):

    def test_sample_jolly(self):
        """Classic sample: 1 4 2 3 is Jolly."""
        self.assertTrue(is_jolly_sequence([1, 4, 2, 3]))
        self.assertEqual(judge_line(4, [1, 4, 2, 3]), "Jolly")

    def test_sample_not_jolly(self):
        """Classic sample: 1 4 2 -1 6 is Not jolly."""
        self.assertFalse(is_jolly_sequence([1, 4, 2, -1, 6]))
        self.assertEqual(judge_line(5, [1, 4, 2, -1, 6]), "Not jolly")

    def test_single_number_is_jolly(self):
        """Length 1 has no differences, so it is Jolly."""
        self.assertTrue(is_jolly_sequence([42]))
        self.assertEqual(judge_line(1, [42]), "Jolly")

    def test_two_numbers_diff_one(self):
        """For n=2, only difference 1 is valid."""
        self.assertTrue(is_jolly_sequence([10, 11]))
        self.assertEqual(judge_line(2, [10, 11]), "Jolly")

    def test_two_numbers_diff_not_one(self):
        """For n=2, difference other than 1 is invalid."""
        self.assertFalse(is_jolly_sequence([10, 13]))
        self.assertEqual(judge_line(2, [10, 13]), "Not jolly")

    def test_duplicate_diff_fails(self):
        """Repeated differences mean some required value is missing."""
        self.assertFalse(is_jolly_sequence([1, 3, 5, 7]))

    def test_zero_diff_fails(self):
        """Difference 0 is never allowed."""
        self.assertFalse(is_jolly_sequence([5, 5, 4]))

    def test_diff_too_large_fails(self):
        """Difference larger than n-1 is invalid."""
        self.assertFalse(is_jolly_sequence([1, 100, 2]))

    def test_negative_numbers_jolly(self):
        """Negative values are fine; we only care about absolute diffs."""
        self.assertTrue(is_jolly_sequence([-1, -4, -2, -3]))

    def test_length_mismatch_not_jolly(self):
        """If n does not match actual length, treat as Not jolly."""
        self.assertEqual(judge_line(5, [1, 4, 2, 3]), "Not jolly")


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_solution_10038_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestJollyJumpers10038Manual)
    with log_path.open("w", encoding="utf-8") as log_file:
        runner = unittest.TextTestRunner(stream=log_file, verbosity=2)
        result = runner.run(suite)

        log_file.write("\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"tests_run={result.testsRun}\n")
        log_file.write(f"failures={len(result.failures)}\n")
        log_file.write(f"errors={len(result.errors)}\n")
        log_file.write(f"success={result.wasSuccessful()}\n")

    print("Tests finished.")
    print(f"Log saved to: {log_path.name}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
