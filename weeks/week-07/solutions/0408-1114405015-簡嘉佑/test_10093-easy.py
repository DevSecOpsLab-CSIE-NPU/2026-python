"""
測試程式：solution_10093-easy.py

簡易版本的測試程式。
"""

from __future__ import annotations

from pathlib import Path
import unittest
import importlib.util


def load_easy_solution():
    """動態載入 solution_10093-easy.py（因檔名含 '-'）。"""
    path = Path(__file__).resolve().parent / "solution_10093-easy.py"
    spec = importlib.util.spec_from_file_location("solution_10093_easy", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


solution_easy = load_easy_solution()


def solve_naive(n: int, m: int, grid: list[str]) -> int:
    """
    暴力解法（回溯）。
    """
    max_artillery = [0]

    def can_place(r: int, c: int, placed: list[tuple]) -> bool:
        if grid[r][c] == "H":
            return False
        for pr, pc in placed:
            if abs(pr - r) <= 2 and abs(pc - c) <= 2 and (pr != r or pc != c):
                return False
        return True

    def backtrack(row: int, placed: list[tuple]) -> None:
        if row == n:
            max_artillery[0] = max(max_artillery[0], len(placed))
            return

        def gen_row_configs(col: int, current: list[tuple]) -> None:
            if col == m:
                backtrack(row + 1, placed + current)
                return

            gen_row_configs(col + 1, current)

            if can_place(row, col, placed + current):
                gen_row_configs(col + 1, current + [(row, col)])

        gen_row_configs(0, [])

    backtrack(0, [])
    return max_artillery[0]


class TestArtillery10093Easy(unittest.TestCase):
    """測試簡易版砲兵部隊部署。"""

    def test_single_cell(self):
        """1×1 全平原。"""
        result = solution_easy.solve(1, 1, ["P"])
        self.assertEqual(result, 1)

    def test_single_row_3(self):
        """1×3 全平原。距離限制 >= 3，所以最多 1 支。"""
        result = solution_easy.solve(1, 3, ["PPP"])
        self.assertEqual(result, 1)

    def test_2x3_small(self):
        """2×3 小網格。"""
        grid = ["PPP", "PPP"]
        result = solution_easy.solve(2, 3, grid)
        expected = solve_naive(2, 3, grid)
        self.assertEqual(result, expected)

    def test_3x3_medium(self):
        """3×3 中等網格。"""
        grid = ["PPP", "PPP", "PPP"]
        result = solution_easy.solve(3, 3, grid)
        expected = solve_naive(3, 3, grid)
        self.assertEqual(result, expected)


def run_tests() -> bool:
    """執行所有測試並輸出 LOG。"""
    log_path = Path(__file__).resolve().parent / "test_10093-easy.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestArtillery10093Easy)
    with log_path.open("w", encoding="utf-8") as log_file:
        runner = unittest.TextTestRunner(stream=log_file, verbosity=2)
        result = runner.run(suite)

        log_file.write("\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"tests_run={result.testsRun}\n")
        log_file.write(f"failures={len(result.failures)}\n")
        log_file.write(f"errors={len(result.errors)}\n")
        log_file.write(f"success={result.wasSuccessful()}\n")

    print("Easy tests finished.")
    print(f"Log saved to: {log_path.name}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
