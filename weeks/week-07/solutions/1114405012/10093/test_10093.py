"""10093（炮兵部署）單元測試。"""

import importlib.util
import os
import subprocess
import sys
import unittest
from pathlib import Path


DEFAULT_FILE = "10093.py"


def normalize(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines()).strip()


def brute_max(grid):
    n = len(grid)
    m = len(grid[0]) if n else 0

    best = 0
    used = []

    def can_place(r, c):
        if grid[r][c] == "H":
            return False
        for rr, cc in used:
            if rr == r and abs(cc - c) <= 2:
                return False
            if cc == c and abs(rr - r) <= 2:
                return False
        return True

    def dfs(idx, cnt):
        nonlocal best
        if idx == n * m:
            best = max(best, cnt)
            return
        r = idx // m
        c = idx % m

        # 不放
        dfs(idx + 1, cnt)

        # 放
        if can_place(r, c):
            used.append((r, c))
            dfs(idx + 1, cnt + 1)
            used.pop()

    dfs(0, 0)
    return best


class Runner:
    def __init__(self):
        base = Path(__file__).resolve().parent
        env = os.environ.get("SOLUTION_FILE")
        self.path = (base / DEFAULT_FILE) if not env else Path(env).resolve()
        if not self.path.exists():
            raise FileNotFoundError(f"找不到解答檔：{self.path}")

    def run(self, input_data: str) -> str:
        mod = self._load_module(self.path)
        if mod is not None and hasattr(mod, "solve"):
            out = mod.solve(input_data)
            return normalize(str(out))

        proc = subprocess.run(
            [sys.executable, str(self.path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr)
        return normalize(proc.stdout)

    @staticmethod
    def _load_module(path: Path):
        try:
            spec = importlib.util.spec_from_file_location("student_solution_10093", path)
            if spec is None or spec.loader is None:
                return None
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
        except Exception:
            return None


class Test10093(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = Runner()

    def check_grid(self, grid):
        n = len(grid)
        m = len(grid[0])
        inp = f"{n} {m}\n" + "\n".join(grid) + "\n"
        expected = str(brute_max(grid))
        got = self.runner.run(inp)
        self.assertEqual(got, expected)

    def test_all_plain_small(self):
        self.check_grid(["PPP", "PPP", "PPP"])

    def test_with_mountains(self):
        self.check_grid(["PHPP", "PPHP", "HPPP"])

    def test_single_row(self):
        self.check_grid(["PPPPPP"])

    def test_small_random_like(self):
        self.check_grid(["PHPP", "HPPP", "PPHP", "PPPP"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
