import unittest
from io import StringIO
import sys
from D2_easy import main as process_data

def run_with_input(input_text):
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(input_text)
    sys.stdout = StringIO()
    try:
        process_data()
        return sys.stdout.getvalue()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

class TestD2Processing(unittest.TestCase):

    def test_sample_input_1(self):
        input_data = "8\n4 7 4 2 9 2 6 7\n0\n"
        output = run_with_input(input_data)
        self.assertEqual(output.strip(), "2 4 6")

    def test_no_even_numbers(self):
        input_data = "5\n1 3 5 7 9\n0\n"
        output = run_with_input(input_data)
        self.assertEqual(output.strip(), "NONE")

    def test_single_even_number(self):
        input_data = "1\n-8\n0\n"
        output = run_with_input(input_data)
        self.assertEqual(output.strip(), "-8")


if __name__ == "__main__":
    unittest.main()
