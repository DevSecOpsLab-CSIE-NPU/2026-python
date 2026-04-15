import subprocess
import sys
import unittest
from pathlib import Path


class TestRainUmbrellaProblem(unittest.TestCase):
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

    def test_no_umbrella(self):
        input_data = """0 10 5 2
"""
        expected_output = "100.00"
        self.check_all_versions(input_data, expected_output)

    def test_full_cover_static(self):
        input_data = """1 10 5 3
0 10 0
"""
        expected_output = "0.00"
        self.check_all_versions(input_data, expected_output)

    def test_single_partial_static(self):
        input_data = """1 10 5 2
3 4 0
"""
        expected_output = "60.00"
        self.check_all_versions(input_data, expected_output)

    def test_two_static_disjoint(self):
        input_data = """2 10 5 1
0 3 0
5 2 0
"""
        expected_output = "25.00"
        self.check_all_versions(input_data, expected_output)

    def test_two_static_overlap(self):
        input_data = """2 10 5 1
0 4 0
2 4 0
"""
        expected_output = "30.00"
        self.check_all_versions(input_data, expected_output)

    def test_two_moving_toward_each_other(self):
        input_data = """2 10 3 1
0 4 1
6 4 -1
"""
        expected_output = "10.00"
        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()