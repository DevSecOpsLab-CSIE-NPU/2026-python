import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
Q = BASE / "q10093.py"
EASY = BASE / "q10093-easy.py"


def run_prog(path: Path, data: str) -> str:
    p = subprocess.run([sys.executable, str(path)], input=data, text=True, capture_output=True, check=True, cwd=str(BASE))
    return p.stdout.strip()


class TestQ10093(unittest.TestCase):
    def test_main(self) -> None:
        data = "3 3\nPPP\nPHP\nPPP\n"
        out = run_prog(Q, data)
        self.assertEqual(out, "3")

    def test_easy(self) -> None:
        data = "3 3\nPPP\nPHP\nPPP\n"
        out = run_prog(EASY, data)
        self.assertEqual(out, "3")


if __name__ == "__main__":
    unittest.main(verbosity=2)
