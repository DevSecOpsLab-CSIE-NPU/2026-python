import subprocess
import sys
import unittest
from pathlib import Path


def run_program(filename: str, input_data: str) -> str:
    program = Path(__file__).with_name(filename)
    result = subprocess.run(
        [sys.executable, str(program)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test12019HandTyped(unittest.TestCase):
    def test_hand(self) -> None:
        input_data = """2
1 1
8 9
"""
        expected = """Sunday
Thursday"""
        self.assertEqual(run_program("q12019-Hand-typed.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
