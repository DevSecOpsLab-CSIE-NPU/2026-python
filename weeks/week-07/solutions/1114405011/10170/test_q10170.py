import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
Q = BASE / "q10170.py"
EASY = BASE / "q10170-easy.py"


def run_prog(path: Path, data: str) -> str:
    p = subprocess.run([sys.executable, str(path)], input=data, text=True, capture_output=True, check=True, cwd=str(BASE))
    return p.stdout.strip()


class TestQ10170(unittest.TestCase):
    def test_main(self) -> None:
        self.assertEqual(run_prog(Q, "3 8\n"), "5")

    def test_easy(self) -> None:
        self.assertEqual(run_prog(EASY, "3 8\n"), "5")


if __name__ == "__main__":
    unittest.main(verbosity=2)
