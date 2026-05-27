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


class TestQuestion11417(unittest.TestCase):
    def test_sample(self) -> None:
        input_data = """10
100
500
0
"""
        expected = """67
13015
442011"""
        self.assertEqual(run_program("question_11417.py", input_data), expected)

    def test_small_values(self) -> None:
        input_data = """2
3
0
"""
        expected = """1
3"""
        self.assertEqual(run_program("question_11417.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
