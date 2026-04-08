import random
import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
TARGET = BASE / "q10093-Hand-typed.py"


def run_prog(inp: str) -> str:
    p = subprocess.run([sys.executable, str(TARGET)], input=inp, text=True, capture_output=True, check=True, cwd=str(BASE))
    return p.stdout.strip()


def brute(board: list[str]) -> int:
    n = len(board)
    m = len(board[0])
    plains = [(r, c) for r in range(n) for c in range(m) if board[r][c] == "P"]
    best = 0
    for mask in range(1 << len(plains)):
        pick = [plains[i] for i in range(len(plains)) if (mask >> i) & 1]
        ok = True
        for i in range(len(pick)):
            r1, c1 = pick[i]
            for j in range(i + 1, len(pick)):
                r2, c2 = pick[j]
                if r1 == r2 and abs(c1 - c2) <= 2:
                    ok = False
                    break
                if c1 == c2 and abs(r1 - r2) <= 2:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            best = max(best, len(pick))
    return best


class TestQ10093HandTyped(unittest.TestCase):
    def test_fixed(self) -> None:
        data = "3 3\nPPP\nPHP\nPPP\n"
        out = run_prog(data)
        self.assertEqual(int(out), brute(["PPP", "PHP", "PPP"]))

    def test_random_small(self) -> None:
        random.seed(10093)
        for n in range(1, 4):
            for m in range(1, 5):
                for _ in range(8):
                    board = []
                    for _r in range(n):
                        board.append("".join("P" if random.random() < 0.7 else "H" for _c in range(m)))
                    inp = f"{n} {m}\n" + "\n".join(board) + "\n"
                    out = run_prog(inp)
                    self.assertEqual(int(out), brute(board))


if __name__ == "__main__":
    unittest.main(verbosity=2)
