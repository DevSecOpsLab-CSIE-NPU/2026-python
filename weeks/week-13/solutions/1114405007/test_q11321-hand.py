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


class TestQ11321Hand(unittest.TestCase):
    def test_first_trap_ok(self):
        result = run("q11321-hand.py", "3 3 1\n1 1\n")
        self.assertEqual(result, "<(_ _)>")

    def test_blocking_column(self):
        result = run("q11321-hand.py", "3 3 3\n0 1\n1 1\n2 1\n")
        lines = result.splitlines()
        self.assertEqual(lines[0], "<(_ _)>")
        self.assertEqual(lines[1], "<(_ _)>")
        self.assertEqual(lines[2], ">_<")

    def test_same_as_easy(self):
        data = "3 3 4\n0 1\n1 1\n2 1\n1 2\n"
        self.assertEqual(
            run("q11321-hand.py", data),
            run("q11321-easy.py", data),
        )


if __name__ == "__main__":
    unittest.main()
