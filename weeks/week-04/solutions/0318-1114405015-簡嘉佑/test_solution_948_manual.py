"""
UVA 948 - Fake Coin Detection
Unit tests for solution_948_manual.py (find_fake)
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_948_manual import find_fake


class TestFakeCoin948Manual(unittest.TestCase):

    def test_light_fake_on_left(self):
        """Fake coin is light and placed on the left side."""
        weighings = [([1], [2], "<"), ([1], [3], "<")]
        self.assertEqual(find_fake(3, weighings), 1)

    def test_heavy_fake_on_right(self):
        """Fake coin is heavy and placed on the right side."""
        weighings = [([1], [3], "<"), ([2], [3], "<")]
        self.assertEqual(find_fake(3, weighings), 3)

    def test_equal_weighings_narrow_down(self):
        """Equal results eliminate coins; remaining weighing confirms fake."""
        weighings = [
            ([1], [2], "="),
            ([3], [4], "<"),
            ([3], [1], "<"),
        ]
        self.assertEqual(find_fake(4, weighings), 3)

    def test_ambiguous_returns_zero(self):
        """Not enough information to identify the fake coin uniquely."""
        weighings = [([1, 2], [3, 4], "<")]
        self.assertEqual(find_fake(4, weighings), 0)

    def test_single_coin_no_weighings(self):
        """N=1 with no weighings: the only coin must be fake."""
        self.assertEqual(find_fake(1, []), 1)

    def test_heavy_fake_coin(self):
        """Fake coin is heavy; both weighings show left heavy (>)."""
        weighings = [([2], [1], ">"), ([2], [3], ">")]
        self.assertEqual(find_fake(3, weighings), 2)

    def test_all_equal_fake_not_weighed(self):
        """All results are equal; fake coin was never placed on the scale."""
        weighings = [
            ([1], [2], "="),
            ([3], [4], "="),
            ([1, 3], [2, 4], "="),
        ]
        self.assertEqual(find_fake(5, weighings), 5)

    def test_multiple_weighings_unique(self):
        """Three weighings narrow down to coin 4 being heavy."""
        weighings = [
            ([1, 2], [3, 4], "<"),
            ([1, 3], [2, 4], "<"),
            ([4],    [5],    ">"),
        ]
        self.assertEqual(find_fake(6, weighings), 4)


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_solution_948_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestFakeCoin948Manual)
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
