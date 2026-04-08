"""10093 單元測試。

使用小地圖的暴力搜尋當作標準答案，
比對正式版、easy 版與手打版的輸出。
"""

from __future__ import annotations

import importlib.util
import random
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_module(filename: str):
    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def build_input(grid):
    return f"{len(grid)} {len(grid[0])}\n" + "\n".join(grid) + "\n"


def brute_force(grid):
    rows = len(grid)
    cols = len(grid[0])
    cells = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "P":
                cells.append((r, c))

    best = 0
    total = 1 << len(cells)
    for mask in range(total):
        chosen = []
        for index, cell in enumerate(cells):
            if mask & (1 << index):
                chosen.append(cell)

        ok = True
        for i in range(len(chosen)):
            r1, c1 = chosen[i]
            for j in range(i):
                r2, c2 = chosen[j]
                if r1 == r2 and abs(c1 - c2) <= 2:
                    ok = False
                    break
                if c1 == c2 and abs(r1 - r2) <= 2:
                    ok = False
                    break
            if not ok:
                break

        if ok:
            best = max(best, len(chosen))

    return str(best)


class Test10093(unittest.TestCase):
    def setUp(self):
        self.normal = load_module("10093.py")
        self.easy = load_module("10093-easy.py")
        self.hand = load_module("10093-hand.py")

    def assert_all(self, grid):
        text = build_input(grid)
        expected = brute_force(grid)
        self.assertEqual(self.normal.solve(text), expected)
        self.assertEqual(self.easy.solve(text), expected)
        self.assertEqual(self.hand.solve(text), expected)

    def test_small_grids(self):
        self.assert_all(["P"])
        self.assert_all(["PP", "PP"])
        self.assert_all(["PHP", "PPP", "HPH"])

    def test_random_grids(self):
        random.seed(10093)
        for rows in range(1, 5):
            for cols in range(1, 5):
                for _ in range(5):
                    grid = []
                    for _row in range(rows):
                        row = "".join(random.choice("PH") for _ in range(cols))
                        grid.append(row)
                    self.assert_all(grid)

    def test_empty_input(self):
        self.assertEqual(self.normal.solve(""), "")
        self.assertEqual(self.easy.solve(""), "")
        self.assertEqual(self.hand.solve(""), "")


if __name__ == "__main__":
    unittest.main()