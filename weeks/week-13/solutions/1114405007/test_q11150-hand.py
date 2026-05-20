import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
PY = sys.executable


def run(filename, input_data):
    proc = subprocess.run(
        [PY, str(BASE / filename)],
        input=input_data, text=True, capture_output=True, check=True,
    )
    return proc.stdout.strip()


class TestQ11150Hand(unittest.TestCase):
    def test_basic_no_stone(self):
        result = run("q11150-hand.py", "10\n2 3 1\n5\n")
        self.assertEqual(result, "0")

    def test_basic_with_stone(self):
        result = run("q11150-hand.py", "10\n1 2 1\n1\n")
        self.assertEqual(result, "0")

    def test_same_as_easy(self):
        data = "10\n2 3 3\n2 4 7\n"
        self.assertEqual(
            run("q11150-hand.py", data),
            run("q11150-easy.py", data),
        )

    def test_fixed_step(self):
        result = run("q11150-hand.py", "10\n3 3 2\n3 6\n")
        self.assertEqual(result, "2")


if __name__ == "__main__":
    unittest.main()
