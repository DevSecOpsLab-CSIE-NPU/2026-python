import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
TARGET = BASE / "q10101-Hand-typed.py"


def run_prog(inp: str) -> str:
    p = subprocess.run([sys.executable, str(TARGET)], input=inp, text=True, capture_output=True, check=True, cwd=str(BASE))
    return p.stdout.strip()


def eval_side(side: str) -> int:
    i = 0
    sign = 1
    if i < len(side) and side[i] == "-":
        sign = -1
        i += 1
    total = 0
    while i < len(side):
        j = i
        while j < len(side) and side[j].isdigit():
            j += 1
        total += sign * int(side[i:j])
        if j >= len(side):
            break
        sign = 1 if side[j] == "+" else -1
        i = j + 1
    return total


class TestQ10101HandTyped(unittest.TestCase):
    def test_has_solution(self) -> None:
        out = run_prog("1+1=3#\n")
        self.assertTrue(out.endswith("#"))
        expr = out[:-1]
        l, r = expr.split("=")
        self.assertEqual(eval_side(l), eval_side(r))

    def test_no_solution(self) -> None:
        out = run_prog("1=1#\n")
        self.assertEqual(out, "No")


if __name__ == "__main__":
    unittest.main(verbosity=2)
