"""
UVA 100 - The 3n + 1 Problem
Unit tests for solution_100_manual.py
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_100_manual import cycle_length, format_output_line, max_cycle_length


class TestUVA100Manual(unittest.TestCase):

    def test_cycle_length_base_case(self):
        """n=1 should have cycle length 1."""
        self.assertEqual(cycle_length(1, {1: 1}), 1)

    def test_cycle_length_sample_22(self):
        """From statement: cycle length of 22 is 16."""
        self.assertEqual(cycle_length(22, {1: 1}), 16)

    def test_sample_case_1_10(self):
        """Classic sample: 1 10 => 20."""
        self.assertEqual(max_cycle_length(1, 10), 20)
        self.assertEqual(format_output_line(1, 10), "1 10 20")

    def test_sample_case_100_200(self):
        """Classic sample: 100 200 => 125."""
        self.assertEqual(max_cycle_length(100, 200), 125)
        self.assertEqual(format_output_line(100, 200), "100 200 125")

    def test_sample_case_201_210(self):
        """Classic sample: 201 210 => 89."""
        self.assertEqual(max_cycle_length(201, 210), 89)
        self.assertEqual(format_output_line(201, 210), "201 210 89")

    def test_sample_case_900_1000(self):
        """Classic sample: 900 1000 => 174."""
        self.assertEqual(max_cycle_length(900, 1000), 174)
        self.assertEqual(format_output_line(900, 1000), "900 1000 174")

    def test_reversed_interval(self):
        """When i > j, computation still uses normalized interval."""
        self.assertEqual(max_cycle_length(10, 1), 20)
        self.assertEqual(format_output_line(10, 1), "10 1 20")

    def test_single_value_interval(self):
        """When i == j, answer equals that number's cycle length."""
        self.assertEqual(max_cycle_length(7, 7), cycle_length(7, {1: 1}))
        self.assertEqual(format_output_line(7, 7), f"7 7 {cycle_length(7, {1: 1})}")

    def test_memoization_reuse(self):
        """Repeated queries should reuse memoized values consistently."""
        memo = {1: 1}
        a = cycle_length(13, memo)
        b = cycle_length(13, memo)
        self.assertEqual(a, b)
        self.assertIn(13, memo)


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_solution_100_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA100Manual)
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
