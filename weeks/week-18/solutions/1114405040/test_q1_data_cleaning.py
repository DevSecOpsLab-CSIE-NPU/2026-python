import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("q1_data_cleaning.py")


class TestQ1DataCleaning(unittest.TestCase):
    def run_program(self, text):
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input=text,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout

    def test_sample_and_none_case(self):
        data = "8\n4 7 4 2 9 2 6 7\n3\n1 3 5\n0\n"
        self.assertEqual(self.run_program(data), "2 4 6\nNONE")

    def test_duplicates_keep_first_then_sort(self):
        data = "7\n8 4 8 2 4 6 2\n0\n"
        self.assertEqual(self.run_program(data), "2 4 6 8")

    def test_stop_at_zero(self):
        data = "0\n5\n2 4 6 8 10\n"
        self.assertEqual(self.run_program(data), "")


if __name__ == "__main__":
    unittest.main()
