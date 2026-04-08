import random
import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
TARGET = BASE / "q10071-Hand-typed.py"


def run_prog(inp: str) -> str:
    p = subprocess.run([sys.executable, str(TARGET)], input=inp, text=True, capture_output=True, check=True, cwd=str(BASE))
    return p.stdout.strip()


def brute(vals: list[int]) -> int:
    total = 0
    for a in vals:
        for b in vals:
            for c in vals:
                for d in vals:
                    for e in vals:
                        for f in vals:
                            if a + b + c + d + e == f:
                                total += 1
    return total


class TestQ10071HandTyped(unittest.TestCase):
    def test_fixed(self) -> None:
        out = run_prog("3\n-1\n0\n1\n")
        self.assertEqual(out, str(brute([-1, 0, 1])))

    def test_random(self) -> None:
        random.seed(10071)
        pool = list(range(-4, 5))
        for _ in range(10):
            random.shuffle(pool)
            vals = sorted(pool[:4])
            inp = str(len(vals)) + "\n" + "\n".join(map(str, vals)) + "\n"
            out = run_prog(inp)
            self.assertEqual(int(out), brute(vals))


if __name__ == "__main__":
    unittest.main(verbosity=2)
