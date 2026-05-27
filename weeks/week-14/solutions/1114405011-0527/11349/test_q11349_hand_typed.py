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


class Test11349HandTyped(unittest.TestCase):
    def test_hand_typed(self) -> None:
        input_data = """2
N = 2
1 2
2 1
N = 2
1 0
2 1
"""
        expected = """Test #1: Symmetric.
Test #2: Non-symmetric."""
        self.assertEqual(run_program("q11349-Hand-typed.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
