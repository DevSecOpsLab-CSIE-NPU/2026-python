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


class TestQuestion11461(unittest.TestCase):
    def test_sample(self) -> None:
        input_data = """1 4
1 10
1 100000
0 0
"""
        expected = """2
3
316"""
        self.assertEqual(run_program("question_11461.py", input_data), expected)

    def test_edge_cases(self) -> None:
        input_data = """1 1
2 2
3 9
0 0
"""
        expected = """1
0
2"""
        self.assertEqual(run_program("question_11461.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
