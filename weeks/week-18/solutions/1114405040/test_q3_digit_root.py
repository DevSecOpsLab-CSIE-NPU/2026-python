import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("q3_digit_root.py")


class TestQ3DigitRoot(unittest.TestCase):
    def run_program(self, text):
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input=text,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout

    def test_sample_63(self):
        self.assertEqual(self.run_program("63\n"), "1")

    def test_zero(self):
        self.assertEqual(self.run_program("0\n"), "0")

    def test_values_below_and_equal_base(self):
        data = "1\n2\n3\n"
        self.assertEqual(self.run_program(data), "1\n1\n1")

    def test_multiple_inputs_and_large_number(self):
        data = "1000000000\n1\n2\n3\n"
        self.assertEqual(self.run_program(data), "1\n1\n1\n1")


if __name__ == "__main__":
    unittest.main()
