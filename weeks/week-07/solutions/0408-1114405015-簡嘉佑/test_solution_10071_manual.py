"""
Test program for solution_10071_manual.py.
"""

from __future__ import annotations

from pathlib import Path
import unittest

from solution_10071_manual import count_tuples


def count_tuples_naive(values):
    """Naive O(N^6) method for validation."""
    total = 0
    for a in values:
        for b in values:
            for c in values:
                for d in values:
                    for e in values:
                        for f in values:
                            if a + b + c + d + e == f:
                                total += 1
    return total


class TestManualSolution10071(unittest.TestCase):
    def test_single_zero(self):
        self.assertEqual(count_tuples([0]), 1)

    def test_case_1(self):
        arr = [0, 1]
        self.assertEqual(count_tuples(arr), count_tuples_naive(arr))

    def test_case_2(self):
        arr = [-1, 0, 1]
        self.assertEqual(count_tuples(arr), count_tuples_naive(arr))

    def test_case_3(self):
        arr = [1, 2, 3]
        self.assertEqual(count_tuples(arr), count_tuples_naive(arr))

    def test_scale_invariance(self):
        arr1 = [1, 2, 3]
        arr2 = [2, 4, 6]
        self.assertEqual(count_tuples(arr1), count_tuples(arr2))


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_solution_10071_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestManualSolution10071)
    with log_path.open("w", encoding="utf-8") as log_file:
        runner = unittest.TextTestRunner(stream=log_file, verbosity=2)
        result = runner.run(suite)

        log_file.write("\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"tests_run={result.testsRun}\n")
        log_file.write(f"failures={len(result.failures)}\n")
        log_file.write(f"errors={len(result.errors)}\n")
        log_file.write(f"success={result.wasSuccessful()}\n")

    print("Test execution finished.")
    print(f"Log file: {log_path.name}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
