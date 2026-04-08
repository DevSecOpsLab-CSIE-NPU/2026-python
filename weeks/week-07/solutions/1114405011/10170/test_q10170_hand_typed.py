import random
import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
TARGET = BASE / "q10170-Hand-typed.py"


def run_prog(inp: str) -> str:
    p = subprocess.run([sys.executable, str(TARGET)], input=inp, text=True, capture_output=True, check=True, cwd=str(BASE))
    return p.stdout.strip()


def brute(s: int, d: int) -> int:
    day = 0
    g = s
    while True:
        day += g
        if day >= d:
            return g
        g += 1


class TestQ10170HandTyped(unittest.TestCase):
    def test_fixed(self) -> None:
        out = run_prog("3 8\n")
        self.assertEqual(out, "5")

    def test_random(self) -> None:
        random.seed(10170)
        for _ in range(50):
            s = random.randint(1, 30)
            d = random.randint(1, 2000)
            out = run_prog(f"{s} {d}\n")
            self.assertEqual(int(out), brute(s, d))


if __name__ == "__main__":
    unittest.main(verbosity=2)
