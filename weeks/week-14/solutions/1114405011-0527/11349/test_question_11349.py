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


class TestQuestion11349(unittest.TestCase):
    def test_sample(self) -> None:
        input_data = """2
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5
"""
        expected = """Test #1: Symmetric.
Test #2: Non-symmetric."""
        self.assertEqual(run_program("question_11349.py", input_data), expected)

    def test_negative_and_single(self) -> None:
        input_data = """3
N = 1
0
N = 2
1 2
2 1
N = 2
1 -1
-1 1
"""
        expected = """Test #1: Symmetric.
Test #2: Symmetric.
Test #3: Non-symmetric."""
        self.assertEqual(run_program("question_11349.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
