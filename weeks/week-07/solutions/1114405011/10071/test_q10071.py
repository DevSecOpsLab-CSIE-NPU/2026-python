import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
Q = BASE / "q10071.py"
EASY = BASE / "q10071-easy.py"


def run_prog(path: Path, data: str) -> str:
    p = subprocess.run([sys.executable, str(path)], input=data, text=True, capture_output=True, check=True, cwd=str(BASE))
    return p.stdout.strip()


class TestQ10071(unittest.TestCase):
    def test_main(self) -> None:
        data = "3\n-1\n0\n1\n"
        out = run_prog(Q, data)
        self.assertEqual(out, "141")

    def test_easy(self) -> None:
        data = "3\n-1\n0\n1\n"
        out = run_prog(EASY, data)
        self.assertEqual(out, "141")


if __name__ == "__main__":
    unittest.main(verbosity=2)
