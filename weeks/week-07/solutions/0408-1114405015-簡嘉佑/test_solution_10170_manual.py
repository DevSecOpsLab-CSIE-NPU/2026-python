"""
Test program for solution_10170_manual.py
"""

from __future__ import annotations

from pathlib import Path
import unittest

from solution_10170_manual import solve_hotel, total_days_from_s_to_x


def brute_solve(s: int, d: int) -> int:
    """Naive solver for cross-checking small inputs."""
    people = s
    days = 0
    while True:
        days += people
        if days >= d:
            return people
        people += 1


class TestHotel10170Manual(unittest.TestCase):
    def test_known_case_1(self):
        self.assertEqual(solve_hotel(4, 10), 6)

    def test_known_case_2(self):
        self.assertEqual(solve_hotel(1, 1), 1)

    def test_first_group_last_day(self):
        self.assertEqual(solve_hotel(7, 7), 7)

    def test_second_group_first_day(self):
        self.assertEqual(solve_hotel(7, 8), 8)

    def test_small_bruteforce_cross_check(self):
        for s in range(1, 15):
            for d in range(1, 600):
                self.assertEqual(solve_hotel(s, d), brute_solve(s, d), f"s={s}, d={d}")

    def test_large_input_property(self):
        s = 10000
        d = 10**15 - 1
        ans = solve_hotel(s, d)
        self.assertLess(total_days_from_s_to_x(s, ans - 1), d)
        self.assertGreaterEqual(total_days_from_s_to_x(s, ans), d)


def run_tests() -> bool:
    """Run tests and save a log file."""
    log_path = Path(__file__).resolve().parent / "test_solution_10170_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestHotel10170Manual)
    with log_path.open("w", encoding="utf-8") as log_file:
        runner = unittest.TextTestRunner(stream=log_file, verbosity=2)
        result = runner.run(suite)

        log_file.write("\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"tests_run={result.testsRun}\n")
        log_file.write(f"failures={len(result.failures)}\n")
        log_file.write(f"errors={len(result.errors)}\n")
        log_file.write(f"success={result.wasSuccessful()}\n")

    print("Manual tests finished.")
    print(f"Log saved to: {log_path.name}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
