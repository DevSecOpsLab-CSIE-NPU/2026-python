"""
UVA 10019 - Hashmat the Brave Warrior
Unit tests for solution_10019_manual.py (soldier_diff)
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_10019_manual import soldier_diff


class TestSoldierDiff10019Manual(unittest.TestCase):

    def test_basic_smaller_first(self):
        """Smaller number given first; result is b - a."""
        self.assertEqual(soldier_diff(10, 12), 2)

    def test_basic_larger_first(self):
        """Larger number given first; abs ensures positive result."""
        self.assertEqual(soldier_diff(9876543210, 1234567890), 8641975320)

    def test_equal_numbers(self):
        """Both numbers equal; difference is zero."""
        self.assertEqual(soldier_diff(100, 100), 0)

    def test_one_zero(self):
        """One operand is zero; result equals the other number."""
        self.assertEqual(soldier_diff(0, 99), 99)

    def test_both_zero(self):
        """Both operands are zero; result is zero."""
        self.assertEqual(soldier_diff(0, 0), 0)

    def test_large_numbers_diff_one(self):
        """Numbers near 2^63 differing by one."""
        a = 9223372036854775807  # 2^63 - 1
        b = 9223372036854775808  # 2^63
        self.assertEqual(soldier_diff(a, b), 1)

    def test_large_diff(self):
        """Very large absolute difference."""
        self.assertEqual(soldier_diff(1, 9223372036854775808), 9223372036854775807)

    def test_order_independent(self):
        """Result is the same regardless of argument order."""
        self.assertEqual(soldier_diff(3, 7), soldier_diff(7, 3))

    def test_sample_cases(self):
        """Verify common sample inputs from the problem."""
        self.assertEqual(soldier_diff(10, 12), 2)
        self.assertEqual(soldier_diff(1234567890, 9876543210), 8641975320)


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_solution_10019_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSoldierDiff10019Manual)
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
