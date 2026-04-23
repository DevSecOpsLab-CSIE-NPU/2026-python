"""10071 單元測試（繁體中文註解）。"""

import importlib.util
import os
import subprocess
import sys
import unittest
from itertools import product
from pathlib import Path


DEFAULT_FILE = "10071.py"


def normalize(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines()).strip()


def brute_count(s):
    ans = 0
    for a, b, c, d, e, f in product(s, repeat=6):
        if a + b + c + d + e == f:
            ans += 1
    return ans


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
            spec = importlib.util.spec_from_file_location("student_solution_10071", path)
            if spec is None or spec.loader is None:
                return None
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
        except Exception:
            return None


class Test10071(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = Runner()

    def check_set(self, s):
        n = len(s)
        inp = str(n) + "\n" + "\n".join(map(str, s)) + "\n"
        expected = str(brute_count(s))
        got = self.runner.run(inp)
        self.assertEqual(got, expected)

    def test_single(self):
        self.check_set([0])

    def test_small_mixed(self):
        self.check_set([0, 1, -1])

    def test_small_positive(self):
        self.check_set([1, 2, 3])

    def test_small_with_negative(self):
        self.check_set([-2, 0, 4])


if __name__ == "__main__":
    unittest.main(verbosity=2)
