"""10170 單元測試。"""

import importlib.util
import os
import subprocess
import sys
import unittest
from pathlib import Path


DEFAULT_FILE = "10170.py"


def normalize(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines()).strip()


def reference(s: int, d: int) -> int:
    cur = s
    total = s
    while total < d:
        cur += 1
        total += cur
    return cur


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
            spec = importlib.util.spec_from_file_location("student_solution_10170", path)
            if spec is None or spec.loader is None:
                return None
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
        except Exception:
            return None


class Test10170(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = Runner()

    def test_single_case(self):
        s, d = 1, 3
        inp = f"{s} {d}\n"
        self.assertEqual(self.runner.run(inp), str(reference(s, d)))

    def test_multiple_lines(self):
        cases = [(3, 10), (4, 4), (10, 1000), (100, 5050)]
        inp = "\n".join(f"{s} {d}" for s, d in cases) + "\n"
        expected = "\n".join(str(reference(s, d)) for s, d in cases)
        self.assertEqual(self.runner.run(inp), expected)

    def test_large_d(self):
        s, d = 1234, 10**7
        inp = f"{s} {d}\n"
        self.assertEqual(self.runner.run(inp), str(reference(s, d)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
