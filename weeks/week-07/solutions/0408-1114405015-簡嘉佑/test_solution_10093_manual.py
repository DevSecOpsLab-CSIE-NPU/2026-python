"""
Test program for solution_10093_manual.py.
"""

from __future__ import annotations

from pathlib import Path
import unittest

from solution_10093_manual import count_artillery


def count_artillery_naive(n: int, m: int, grid: list[str]) -> int:
    """Naive backtracking for validation."""
    max_count = [0]

    def can_place(r: int, c: int, placed: list[tuple]) -> bool:
        if grid[r][c] == "H":
            return False
        for pr, pc in placed:
            if abs(pr - r) <= 2 and abs(pc - c) <= 2 and (pr != r or pc != c):
                return False
        return True

    def backtrack(row: int, col: int, placed: list[tuple]) -> None:
        if row >= n:
            max_count[0] = max(max_count[0], len(placed))
            return

        next_row = row
        next_col = col + 1
        if next_col >= m:
            next_row += 1
            next_col = 0

        backtrack(next_row, next_col, placed)

        if can_place(row, col, placed):
            backtrack(next_row, next_col, placed + [(row, col)])

    backtrack(0, 0, [])
    return max_count[0]


class TestManualArtillery10093(unittest.TestCase):
    def test_single_cell(self):
        self.assertEqual(count_artillery(1, 1, ["P"]), 1)

    def test_single_mountain(self):
        self.assertEqual(count_artillery(1, 1, ["H"]), 0)

    def test_2x3_small(self):
        grid = ["PPP", "PPP"]
        result = count_artillery(2, 3, grid)
        expected = count_artillery_naive(2, 3, grid)
        self.assertEqual(result, expected)

    def test_3x3_medium(self):
        grid = ["PPP", "PPP", "PPP"]
        result = count_artillery(3, 3, grid)
        expected = count_artillery_naive(3, 3, grid)
        self.assertEqual(result, expected)

    def test_3x4_mixed(self):
        grid = ["PPPP", "PHPH", "PPPP"]
        result = count_artillery(3, 4, grid)
        expected = count_artillery_naive(3, 4, grid)
        self.assertEqual(result, expected)

    def test_4x4_checkerboard(self):
        grid = ["PHPH", "HPHP", "PHPH", "HPHP"]
        result = count_artillery(4, 4, grid)
        expected = count_artillery_naive(4, 4, grid)
        self.assertEqual(result, expected)

    def test_all_mountains(self):
        self.assertEqual(count_artillery(3, 3, ["HHH", "HHH", "HHH"]), 0)

    def test_distance_constraint(self):
        grid = ["P" * 7]
        result = count_artillery(1, 7, grid)
        # With distance > 2 constraint: (0,0) and (0,3) can coexist
        # Possible placements: (0,0), (0,3), (0,6) = 3 cannons
        self.assertEqual(result, 3)


def run_tests() -> bool:
    """Run tests and save to log file."""
    log_path = Path(__file__).resolve().parent / "test_solution_10093_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestManualArtillery10093)
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
