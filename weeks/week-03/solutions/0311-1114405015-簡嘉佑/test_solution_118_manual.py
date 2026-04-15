"""
UVA 118 - Mutant Flatworld Explorers
Unit tests for solution_118_manual.py
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_118_manual import (
    format_robot_result,
    simulate_robot,
    turn_left,
    turn_right,
)


class TestUVA118Manual(unittest.TestCase):

    def test_turn_left_right_cycle(self):
        """Turning must follow N-E-S-W cycle."""
        self.assertEqual(turn_left("N"), "W")
        self.assertEqual(turn_right("N"), "E")
        d = "N"
        for _ in range(4):
            d = turn_right(d)
        self.assertEqual(d, "N")

    def test_simple_move_inside(self):
        """A normal forward move inside boundary should not be lost."""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = simulate_robot(5, 3, 1, 1, "E", "F", scents)
        self.assertEqual((x, y, d, lost), (2, 1, "E", False))

    def test_lost_at_boundary(self):
        """Moving outside boundary should mark robot as LOST."""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = simulate_robot(5, 3, 5, 3, "N", "F", scents)
        self.assertEqual((x, y, d, lost), (5, 3, "N", True))
        self.assertIn((5, 3, "N"), scents)

    def test_scent_blocks_same_fall(self):
        """Same dangerous move with existing scent must be ignored."""
        scents: set[tuple[int, int, str]] = {(5, 3, "N")}
        x, y, d, lost = simulate_robot(5, 3, 5, 3, "N", "F", scents)
        self.assertEqual((x, y, d, lost), (5, 3, "N", False))

    def test_scent_is_direction_specific(self):
        """Scent from one direction should not block another direction."""
        scents: set[tuple[int, int, str]] = {(5, 3, "N")}
        x, y, d, lost = simulate_robot(5, 3, 5, 3, "E", "F", scents)
        self.assertEqual((x, y, d, lost), (5, 3, "E", True))
        self.assertIn((5, 3, "E"), scents)

    def test_sample_robot_1(self):
        """Classic sample #1."""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = simulate_robot(5, 3, 1, 1, "E", "RFRFRFRF", scents)
        self.assertEqual(format_robot_result(x, y, d, lost), "1 1 E")

    def test_sample_robot_2(self):
        """Classic sample #2 should be LOST."""
        scents: set[tuple[int, int, str]] = set()
        x, y, d, lost = simulate_robot(5, 3, 3, 2, "N", "FRRFLLFFRRFLL", scents)
        self.assertEqual(format_robot_result(x, y, d, lost), "3 3 N LOST")
        self.assertIn((3, 3, "N"), scents)

    def test_sample_robot_3_with_existing_scent(self):
        """Classic sample #3 should be protected by scent."""
        scents: set[tuple[int, int, str]] = {(3, 3, "N")}
        x, y, d, lost = simulate_robot(5, 3, 0, 3, "W", "LLFFFLFLFL", scents)
        self.assertEqual(format_robot_result(x, y, d, lost), "2 3 S")

    def test_multiple_robots_share_scents(self):
        """Scents must be shared across robots."""
        scents: set[tuple[int, int, str]] = set()

        r1 = simulate_robot(2, 2, 1, 2, "N", "F", scents)
        self.assertEqual(r1, (1, 2, "N", True))
        self.assertIn((1, 2, "N"), scents)

        r2 = simulate_robot(2, 2, 1, 2, "N", "F", scents)
        self.assertEqual(r2, (1, 2, "N", False))

    def test_output_format(self):
        """Verify normal and LOST output formats."""
        self.assertEqual(format_robot_result(1, 1, "E", False), "1 1 E")
        self.assertEqual(format_robot_result(3, 3, "N", True), "3 3 N LOST")


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_solution_118_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA118Manual)
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
