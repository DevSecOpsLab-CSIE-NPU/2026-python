import unittest
import subprocess
import sys
from pathlib import Path


class TestMinesweeper(unittest.TestCase):
    def run_program(self, filename, input_data):
        file_path = Path(__file__).resolve().parent / filename
        result = subprocess.run(
            [sys.executable, str(file_path)],
            input=input_data,
            text=True,
            capture_output=True
        )
        self.assertEqual(
            result.returncode, 0,
            msg=f"{filename} 執行失敗：\nSTDERR:\n{result.stderr}"
        )
        return result.stdout.strip()

    def check_all_versions(self, input_data, expected_output):
        expected_output = expected_output.strip()

        for filename in ["main.py", "main-easy.py", "main-handwritten.py"]:
            actual_output = self.run_program(filename, input_data)
            self.assertEqual(
                actual_output,
                expected_output,
                msg=f"{filename} 輸出錯誤"
            )

    def test_sample_case(self):
        input_data = """4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
"""
        expected_output = """Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100"""
        self.check_all_versions(input_data, expected_output)

    def test_single_mine(self):
        input_data = """1 1
*
0 0
"""
        expected_output = """Field #1:
*"""
        self.check_all_versions(input_data, expected_output)

    def test_single_empty(self):
        input_data = """1 1
.
0 0
"""
        expected_output = """Field #1:
0"""
        self.check_all_versions(input_data, expected_output)

    def test_all_empty(self):
        input_data = """2 2
..
..
0 0
"""
        expected_output = """Field #1:
00
00"""
        self.check_all_versions(input_data, expected_output)

    def test_all_mines(self):
        input_data = """2 3
***
***
0 0
"""
        expected_output = """Field #1:
***
***"""
        self.check_all_versions(input_data, expected_output)

    def test_mixed_case(self):
        input_data = """3 3
*..
...
..*
0 0
"""
        expected_output = """Field #1:
*10
121
01*"""
        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()