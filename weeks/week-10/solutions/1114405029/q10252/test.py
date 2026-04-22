import subprocess
import sys
import unittest
from pathlib import Path


class TestZeroJudgeA245(unittest.TestCase):
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
        input_data = """1
3
0 0
1 1
2 2
"""
        expected_output = "4 1"
        self.check_all_versions(input_data, expected_output)

    def test_single_point(self):
        input_data = """1
1
5 -3
"""
        expected_output = "0 1"
        self.check_all_versions(input_data, expected_output)

    def test_two_points(self):
        input_data = """1
2
0 0
2 2
"""
        expected_output = "4 9"
        self.check_all_versions(input_data, expected_output)

    def test_square_four_points(self):
        input_data = """1
4
0 0
0 2
2 0
2 2
"""
        expected_output = "8 9"
        self.check_all_versions(input_data, expected_output)

    def test_same_y_line(self):
        input_data = """1
3
-1 5
2 5
10 5
"""
        expected_output = "11 1"
        self.check_all_versions(input_data, expected_output)

    def test_multiple_cases(self):
        input_data = """3
1
0 0
2
0 0
1 0
3
0 0
1 1
2 2
"""
        expected_output = """0 1
1 2
4 1"""
        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()