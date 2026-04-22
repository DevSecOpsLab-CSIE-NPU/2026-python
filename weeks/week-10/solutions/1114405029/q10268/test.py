import subprocess
import sys
import unittest
from pathlib import Path


class TestZeroJudgeA261(unittest.TestCase):
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
        input_data = """2 100
10 786599
4 786599
60 1844674407370955161
63 9223372036854775807
0 0
"""
        expected_output = """14
21
More than 63 trials needed.
61
63"""
        self.check_all_versions(input_data, expected_output)

    def test_one_floor(self):
        input_data = """1 1
0 0
"""
        expected_output = "1"
        self.check_all_versions(input_data, expected_output)

    def test_one_ball_two_floors(self):
        input_data = """1 2
0 0
"""
        expected_output = "2"
        self.check_all_versions(input_data, expected_output)

    def test_two_balls_three_floors(self):
        input_data = """2 3
0 0
"""
        expected_output = "2"
        self.check_all_versions(input_data, expected_output)

    def test_large_k_large_n(self):
        input_data = """100 9223372036854775807
0 0
"""
        expected_output = "63"
        self.check_all_versions(input_data, expected_output)

    def test_more_than_63(self):
        input_data = """1 100
0 0
"""
        expected_output = "More than 63 trials needed."
        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()