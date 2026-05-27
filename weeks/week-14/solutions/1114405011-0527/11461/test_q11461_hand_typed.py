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


class Test11461HandTyped(unittest.TestCase):
    def test_hand(self) -> None:
        input_data = """1 100
0 0
"""
        expected = "10"
        self.assertEqual(run_program("q11461-Hand-typed.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
