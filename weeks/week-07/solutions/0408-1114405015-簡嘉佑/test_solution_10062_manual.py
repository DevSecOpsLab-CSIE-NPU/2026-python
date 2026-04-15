"""
Test program for solution_10062_manual.py.
All comments and output are kept in English only.
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_10062_manual import solve_cow_order


def build_counts_from_perm(perm):
    counts = []
    for i in range(1, len(perm)):
        counts.append(sum(1 for x in perm[:i] if x < perm[i]))
    return counts


class TestManualSolution10062(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solve_cow_order(4, [0, 1, 2]), [4, 1, 2, 3])

    def test_case_2(self):
        self.assertEqual(solve_cow_order(3, [0, 2]), [2, 1, 3])

    def test_case_3(self):
        self.assertEqual(solve_cow_order(5, [1, 2, 3, 4]), [1, 2, 3, 4, 5])

    def test_round_trip(self):
        perms = [
            [2, 1],
            [3, 1, 2],
            [4, 2, 1, 3],
            [5, 3, 1, 4, 2],
        ]
        for perm in perms:
            counts = build_counts_from_perm(perm)
            self.assertEqual(solve_cow_order(len(perm), counts), perm)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            solve_cow_order(4, [0, 1])

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            solve_cow_order(4, [0, 1, 4])


def run_tests_and_save_log() -> bool:
    log_path = Path.cwd() / "test_solution_10062_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestManualSolution10062)
    with log_path.open("w", encoding="utf-8") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = runner.run(suite)

        f.write("\n")
        f.write("=" * 60 + "\n")
        f.write(f"tests_run={result.testsRun}\n")
        f.write(f"failures={len(result.failures)}\n")
        f.write(f"errors={len(result.errors)}\n")
        f.write(f"success={result.wasSuccessful()}\n")

    print("Test execution finished.")
    print(f"Log file: {log_path}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests_and_save_log()
    raise SystemExit(0 if ok else 1)
