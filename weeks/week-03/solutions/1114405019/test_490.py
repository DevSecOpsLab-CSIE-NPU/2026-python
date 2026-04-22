import unittest
from io import StringIO
import sys
from unittest.mock import patch

def run_490(input_str):
    with patch('sys.stdin', StringIO(input_str)):
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            # Copy the main function here
            lines = [line.rstrip('\n') for line in sys.stdin.readlines()]
            if not lines:
                return
            max_len = max(len(line) for line in lines)
            # Pad lines to max_len with spaces
            padded = [line.ljust(max_len) for line in lines]
            # Rotate 90 degrees clockwise
            # Output has max_len rows, each with len(lines) characters
            for j in range(max_len):
                row_str = ''
                for k in range(len(lines)):
                    row_str += padded[len(lines) - 1 - k][j]
                print(row_str)
        return captured_output.getvalue().strip()

class Test490(unittest.TestCase):

    def test_rotation(self):
        input_str = "HELLO\nWORLD"
        expected = "WH\nOE\nRL\nLL\nDO"
        self.assertEqual(run_490(input_str), expected)

if __name__ == '__main__':
    unittest.main()