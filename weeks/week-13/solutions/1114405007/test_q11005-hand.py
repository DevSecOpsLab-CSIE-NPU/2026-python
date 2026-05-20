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


class TestQ11005Hand(unittest.TestCase):
    def test_single_zero(self):
        costs = "1 " * 36
        data = f"1\n{costs}\n1\n0\n"
        result = run("q11005-hand.py", data)
        self.assertIn("Cheapest base(s) for number 0:", result)

    def test_same_as_easy(self):
        costs = "1 " * 36
        data = f"1\n{costs}\n3\n10\n31\n1000\n"
        self.assertEqual(
            run("q11005-hand.py", data),
            run("q11005-easy.py", data),
        )

    def test_two_cases(self):
        costs = "1 " * 36
        data = f"2\n{costs}\n1\n10\n{costs}\n1\n7\n"
        result = run("q11005-hand.py", data)
        self.assertIn("Case 1:", result)
        self.assertIn("Case 2:", result)


if __name__ == "__main__":
    unittest.main()
