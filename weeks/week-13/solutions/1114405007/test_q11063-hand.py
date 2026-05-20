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


class TestQ11063Hand(unittest.TestCase):
    def test_single_black_pixel(self):
        result = run("q11063-hand.py", "1\n0 0 0\n")
        self.assertEqual(result, "0.0000 0.0000 0.0000\nThe average of Y is 0.0000")

    def test_single_white_pixel(self):
        result = run("q11063-hand.py", "1\n255 255 255\n")
        lines = result.splitlines()
        self.assertTrue(lines[-1].startswith("The average of Y is"))

    def test_same_as_easy(self):
        data = "2\n255 3 192 0 0 0\n255 255 255 10 20 30\n"
        self.assertEqual(
            run("q11063-hand.py", data),
            run("q11063-easy.py", data),
        )


if __name__ == "__main__":
    unittest.main()
