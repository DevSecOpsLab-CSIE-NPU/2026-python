import subprocess
import sys
import unittest
from pathlib import Path

from main import get_divisor, process_numbers


class TestQuestion1(unittest.TestCase):
    def test_get_divisor(self):
        self.assertEqual(get_divisor("1114405017"), 5)
        self.assertEqual(get_divisor("1114405018"), 2)

    def test_process_numbers_remove_duplicate_and_filter(self):
        numbers = [4, 7, 4, 2, 9, 2, 6, 7]
        self.assertEqual(process_numbers(numbers, 5), [])

    def test_main_integration(self):
        script = Path(__file__).resolve().parent / "main.py"
        input_data = "8\n4 7 4 2 9 2 6 7\n3\n1 3 5\n0\n"
        proc = subprocess.run([sys.executable, str(script)], input=input_data.encode(), capture_output=True)
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout.decode().replace('\r\n', '\n').strip(), "NONE\n5")


if __name__ == "__main__":
    unittest.main()
