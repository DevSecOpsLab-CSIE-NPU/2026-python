import random
import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
TARGET = BASE / "q10062-Hand-typed.py"


def run_prog(inp: str) -> str:
    p = subprocess.run([sys.executable, str(TARGET)], input=inp, text=True, capture_output=True, check=True, cwd=str(BASE))
    return p.stdout.strip()


class TestQ10062HandTyped(unittest.TestCase):
    def test_fixed(self) -> None:
        out = run_prog("5\n1\n2\n1\n0\n")
        self.assertEqual(out.splitlines(), ["2", "4", "5", "3", "1"])

    def test_random(self) -> None:
        random.seed(10062)
        for n in range(2, 8):
            for _ in range(10):
                p = list(range(1, n + 1))
                random.shuffle(p)
                arr = [0] * (n + 1)
                for i in range(1, n + 1):
                    arr[i] = sum(1 for x in p[: i - 1] if x < p[i - 1])
                data = [str(n)] + [str(arr[i]) for i in range(2, n + 1)]
                out = run_prog("\n".join(data) + "\n")
                self.assertEqual(list(map(int, out.splitlines())), p)


if __name__ == "__main__":
    unittest.main(verbosity=2)
