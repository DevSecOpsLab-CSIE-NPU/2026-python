import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
Q = BASE / "q10062.py"
EASY = BASE / "q10062-easy.py"


def run_prog(path: Path, data: str) -> str:
    p = subprocess.run([sys.executable, str(path)], input=data, text=True, capture_output=True, check=True, cwd=str(BASE))
    return p.stdout.strip()


class TestQ10062(unittest.TestCase):
    def test_main(self) -> None:
        data = "5\n1\n2\n1\n0\n"
        out = run_prog(Q, data)
        self.assertEqual(out.splitlines(), ["2", "4", "5", "3", "1"])

    def test_easy(self) -> None:
        data = "5\n1\n2\n1\n0\n"
        out = run_prog(EASY, data)
        self.assertEqual(out.splitlines(), ["2", "4", "5", "3", "1"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
