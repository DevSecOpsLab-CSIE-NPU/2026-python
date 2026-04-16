from __future__ import annotations

import itertools
import random
import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SCRIPT_MAIN = BASE_DIR / "QUESTION-10093.py"
SCRIPT_EASY = BASE_DIR / "QUESTION-10093-easy.py"


def run_script(script_path: Path, input_data: str) -> str:
    cp = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return cp.stdout.strip()


def build_input(grid: list[str]) -> str:
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    lines = [f"{n} {m}"] + grid
    return "\n".join(lines) + "\n"


def brute_force_max(grid: list[str]) -> int:
    n = len(grid)
    m = len(grid[0])
    plains = []
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "P":
                plains.append((r, c))

    best = 0
    k = len(plains)

    # 只在小測資使用：枚舉所有子集合，檢查是否互相攻擊
    for mask in range(1 << k):
        pos = []
        cnt = 0
        for i in range(k):
            if (mask >> i) & 1:
                pos.append(plains[i])
                cnt += 1
        if cnt <= best:
            continue

        ok = True
        for i in range(len(pos)):
            r1, c1 = pos[i]
            for j in range(i + 1, len(pos)):
                r2, c2 = pos[j]
                # 同列距離 <=2 或同欄距離 <=2 都會互打
                if r1 == r2 and abs(c1 - c2) <= 2:
                    ok = False
                    break
                if c1 == c2 and abs(r1 - r2) <= 2:
                    ok = False
                    break
            if not ok:
                break

        if ok:
            best = cnt

    return best


class TestQuestion10093(unittest.TestCase):
    def assert_both_scripts(self, grid: list[str]) -> None:
        input_data = build_input(grid)
        expected = str(brute_force_max(grid))
        out_main = run_script(SCRIPT_MAIN, input_data)
        out_easy = run_script(SCRIPT_EASY, input_data)
        self.assertEqual(out_main, expected)
        self.assertEqual(out_easy, expected)

    def test_single_plain(self) -> None:
        self.assert_both_scripts(["P"])

    def test_single_mountain(self) -> None:
        self.assert_both_scripts(["H"])

    def test_small_manual(self) -> None:
        grid = [
            "PPP",
            "PHP",
            "PPP",
        ]
        self.assert_both_scripts(grid)

    def test_random_small_grids(self) -> None:
        rng = random.Random(10093)
        for n in range(1, 5):
            for m in range(1, 6):
                for _ in range(8):
                    cells = [rng.choice(["P", "H"]) for _ in range(n * m)]
                    grid = ["".join(cells[i * m : (i + 1) * m]) for i in range(n)]
                    self.assert_both_scripts(grid)


if __name__ == "__main__":
    unittest.main(verbosity=2)
