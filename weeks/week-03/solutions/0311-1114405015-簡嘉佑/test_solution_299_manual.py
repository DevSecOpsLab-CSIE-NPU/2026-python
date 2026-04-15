"""
UVA 299 - Train Swapping
Unit tests for solution_299_manual.py
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_299_manual import format_output, min_adjacent_swaps, solve_case


class TestUVA299Manual(unittest.TestCase):

    def test_already_sorted(self):
        """Already sorted sequence needs zero swaps."""
        self.assertEqual(min_adjacent_swaps([1, 2, 3, 4, 5]), 0)
        self.assertEqual(solve_case([1, 2, 3, 4, 5]), "Optimal train swapping takes 0 swaps.")

    def test_reverse_order(self):
        """Reverse order needs n*(n-1)/2 swaps."""
        train = [5, 4, 3, 2, 1]
        self.assertEqual(min_adjacent_swaps(train), 10)
        self.assertEqual(solve_case(train), "Optimal train swapping takes 10 swaps.")

    def test_single_element(self):
        """Single element needs zero swaps."""
        self.assertEqual(min_adjacent_swaps([1]), 0)

    def test_empty_train(self):
        """Empty sequence edge case should be zero."""
        self.assertEqual(min_adjacent_swaps([]), 0)

    def test_two_elements_swap_needed(self):
        """Two reversed elements need one adjacent swap."""
        self.assertEqual(min_adjacent_swaps([2, 1]), 1)

    def test_small_random_case(self):
        """Case [3,1,2] has two inversions."""
        self.assertEqual(min_adjacent_swaps([3, 1, 2]), 2)

    def test_statement_style_case(self):
        """Case [1,3,2] has one inversion."""
        self.assertEqual(min_adjacent_swaps([1, 3, 2]), 1)

    def test_larger_case(self):
        """Medium case with multiple inversions."""
        train = [4, 3, 1, 2, 5]
        self.assertEqual(min_adjacent_swaps(train), 5)

    def test_output_format(self):
        """Output format must match the statement exactly."""
        self.assertEqual(format_output(0), "Optimal train swapping takes 0 swaps.")
        self.assertEqual(format_output(7), "Optimal train swapping takes 7 swaps.")


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_solution_299_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA299Manual)
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
