import subprocess
import sys
import unittest
from pathlib import Path


class TestZeroJudgeA228(unittest.TestCase):
    def run_program(self, filename, input_data):
        file_path = Path(__file__).resolve().parent / filename
        result = subprocess.run(
            [sys.executable, str(file_path)],
            input=input_data,
            text=True,
            capture_output=True
        )

        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} 執行失敗：\nSTDERR:\n{result.stderr}"
        )

        return result.stdout.strip()

    def check_all_versions(self, input_data, expected_output):
        for filename in ["main.py", "main-easy.py", "main-handwritten.py"]:
            actual_output = self.run_program(filename, input_data)
            self.assertEqual(
                actual_output,
                expected_output,
                msg=f"{filename} 輸出錯誤"
            )

    def test_sample(self):
        input_data = """3
6 3
1 1 1
1 0 1
1 1 1
1 1 1
1 0 1
1 1 1
2 4
1 1 1 1
1 1 1 1
1 1
0
"""
        expected_output = """Case 1: 3
Case 2: 2
Case 3: 1"""
        self.check_all_versions(input_data, expected_output)

    def test_single_empty_cell(self):
        input_data = """1
1 1
1
"""
        expected_output = "Case 1: 0"
        self.check_all_versions(input_data, expected_output)

    def test_single_socket_cell(self):
        input_data = """1
1 1
0
"""
        expected_output = "Case 1: 1"
        self.check_all_versions(input_data, expected_output)

    def test_two_by_two_all_empty(self):
        input_data = """1
2 2
1 1
1 1
"""
        expected_output = "Case 1: 1"
        self.check_all_versions(input_data, expected_output)

    def test_diagonal_empty_only(self):
        input_data = """1
2 2
1 0
0 1
"""
        expected_output = "Case 1: 0"
        self.check_all_versions(input_data, expected_output)

    def test_compact_row_format(self):
        input_data = """1
2 4
1111
1111
"""
        expected_output = "Case 1: 2"
        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()