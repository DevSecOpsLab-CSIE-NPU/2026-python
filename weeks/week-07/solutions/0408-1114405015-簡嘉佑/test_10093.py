"""
測試程式：solution_10093.py

包含多個測試用例，驗證正式版炮兵部署演算法。
"""

from __future__ import annotations

from pathlib import Path
import unittest

from solution_10093 import solve_artillery


def solve_naive(n: int, m: int, grid: list[str]) -> int:
    """
    暴力解法（回溯）。
    對較小的網格進行窮舉以驗證正確性。
    """
    max_artillery = [0]

    def can_place(r: int, c: int, placed: list[tuple[int, int]]) -> bool:
        """檢查 (r, c) 是否能放置。"""
        if grid[r][c] == "H":
            return False
        for pr, pc in placed:
            # 攻擊範圍：距離在 1 到 2 之間
            if abs(pr - r) <= 2 and abs(pc - c) <= 2 and (pr != r or pc != c):
                return False
        return True

    def backtrack(row: int, placed: list[tuple[int, int]]) -> None:
        """回溯嘗試在每一位置放置炮兵。"""
        if row == n:
            max_artillery[0] = max(max_artillery[0], len(placed))
            return

        # 嘗試在 row 行放置炮兵
        def gen_row_configs(col: int, current: list[tuple[int, int]]) -> None:
            """在 row 行放置部分炮兵，col 是當前考慮的列。"""
            if col == m:
                # 該行配置完成，移至下一行
                backtrack(row + 1, placed + current)
                return

            # 不在 (row, col) 放置
            gen_row_configs(col + 1, current)

            # 在 (row, col) 放置（如果可以）
            if can_place(row, col, placed + current):
                gen_row_configs(col + 1, current + [(row, col)])

        gen_row_configs(0, [])

    backtrack(0, [])
    return max_artillery[0]


class TestArtillery10093(unittest.TestCase):
    """測試砲兵部隊部署。"""

    def test_single_cell(self):
        """1×1 全平原，應該能放 1 支。"""
        result = solve_artillery(1, 1, ["P"])
        self.assertEqual(result, 1)

    def test_single_mountain(self):
        """1×1 全山地，應該能放 0 支。"""
        result = solve_artillery(1, 1, ["H"])
        self.assertEqual(result, 0)

    def test_single_row_5_plain(self):
        """1×5 全平原。攻擊距離 1-2，所以最多放距離 >= 3 的位置，例如 (0,3)、(1,4)，共 2 支。"""
        result = solve_artillery(1, 5, ["PPPPP"])
        self.assertEqual(result, 2)

    def test_single_row_5_mixed(self):
        """1×5 混合地形。"""
        result = solve_artillery(1, 5, ["PHPPH"])
        # P 在位置 0, 2, 4
        # 不能相鄰，最多 2 支（位置 0 和 2）或其他組合
        expected = solve_naive(1, 5, ["PHPPH"])
        self.assertEqual(result, expected)

    def test_2x3_small(self):
        """2×3 小網格測試。"""
        grid = ["PPP", "PPP"]
        result = solve_artillery(2, 3, grid)
        expected = solve_naive(2, 3, grid)
        self.assertEqual(result, expected)

    def test_3x3_medium(self):
        """3×3 中等網格。"""
        grid = ["PPP", "PPP", "PPP"]
        result = solve_artillery(3, 3, grid)
        expected = solve_naive(3, 3, grid)
        self.assertEqual(result, expected)

    def test_3x4_mixed(self):
        """3×4 混合地形。"""
        grid = ["PPPP", "PHPH", "PPPP"]
        result = solve_artillery(3, 4, grid)
        expected = solve_naive(3, 4, grid)
        self.assertEqual(result, expected)

    def test_4x4_checkerboard(self):
        """4×4 棋盤式。"""
        grid = ["PHPH", "HPHP", "PHPH", "HPHP"]
        result = solve_artillery(4, 4, grid)
        expected = solve_naive(4, 4, grid)
        self.assertEqual(result, expected)


def run_tests() -> bool:
    """執行所有測試並輸出 LOG。"""
    log_path = Path(__file__).resolve().parent / "test_10093.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestArtillery10093)
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


if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
