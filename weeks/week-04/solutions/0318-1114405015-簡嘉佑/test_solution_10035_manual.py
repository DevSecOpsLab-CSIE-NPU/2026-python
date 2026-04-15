"""
UVA 10035 - Primary Arithmetic
Unit tests for solution_10035_manual.py
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_10035_manual import count_carries, format_result


class TestCarryCount10035Manual(unittest.TestCase):

    def test_no_carry(self):
        """123 + 456 = 579, no carry in any digit."""
        self.assertEqual(count_carries(123, 456), 0)
        self.assertEqual(format_result(0), "No carry operation.")

    def test_one_carry(self):
        """3 + 8 causes exactly one carry."""
        self.assertEqual(count_carries(3, 8), 1)
        self.assertEqual(format_result(1), "1 carry operation.")

    def test_multiple_carries(self):
        """555 + 555 creates carry in every digit (3 total)."""
        self.assertEqual(count_carries(555, 555), 3)
        self.assertEqual(format_result(3), "3 carry operations.")

    def test_chain_carry(self):
        """999 + 1 creates a carry chain across all digits."""
        self.assertEqual(count_carries(999, 1), 3)

    def test_one_zero(self):
        """Adding zero never creates a carry by itself."""
        self.assertEqual(count_carries(0, 12345), 0)
        self.assertEqual(count_carries(9999, 0), 0)

    def test_different_lengths(self):
        """1 + 99 => carries at ones and tens places."""
        self.assertEqual(count_carries(1, 99), 2)

    def test_large_numbers(self):
        """Each of 9 digits carries in this case."""
        self.assertEqual(count_carries(123456789, 987654321), 9)

    def test_output_format(self):
        """Check all required output string forms."""
        self.assertEqual(format_result(0), "No carry operation.")
        self.assertEqual(format_result(1), "1 carry operation.")
        self.assertEqual(format_result(5), "5 carry operations.")

    def test_sample_cases(self):
        """Typical sample validations."""
        self.assertEqual(count_carries(123, 456), 0)
        self.assertEqual(count_carries(555, 555), 3)


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_solution_10035_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCarryCount10035Manual)
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
