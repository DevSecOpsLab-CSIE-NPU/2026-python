import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10221Satellites(unittest.TestCase):
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

    def test_sample_cases(self):
        input_data = """500 30 deg
700 60 min
200 45 deg
"""
        expected_output = """3633.775503 3592.408346
124.616509 124.614927
5215.043805 5082.035982"""
        self.check_all_versions(input_data, expected_output)

    def test_half_circle(self):
        input_data = """0 180 deg
"""
        expected_output = "20231.856747 12880.000000"
        self.check_all_versions(input_data, expected_output)

    def test_large_angle_use_smaller_one(self):
        input_data = """0 270 deg
"""
        expected_output = "10115.928374 9107.026924"
        self.check_all_versions(input_data, expected_output)

    def test_zero_angle(self):
        input_data = """100 0 deg
"""
        expected_output = "0.000000 0.000000"
        self.check_all_versions(input_data, expected_output)

    def test_minutes_input(self):
        input_data = """0 5400 min
"""
        expected_output = "10115.928374 9107.026924"
        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()