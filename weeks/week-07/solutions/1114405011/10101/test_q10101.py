import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
Q = BASE / "q10101.py"
EASY = BASE / "q10101-easy.py"


def run_prog(path: Path, data: str) -> str:
    p = subprocess.run([sys.executable, str(path)], input=data, text=True, capture_output=True, check=True, cwd=str(BASE))
    return p.stdout.strip()


class TestQ10101(unittest.TestCase):
    def test_main(self) -> None:
        out = run_prog(Q, "1+1=3#\n")
        self.assertTrue(out == "No" or out.endswith("#"))

    def test_easy(self) -> None:
        out = run_prog(EASY, "1+1=3#\n")
        self.assertTrue(out == "No" or out.endswith("#"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
