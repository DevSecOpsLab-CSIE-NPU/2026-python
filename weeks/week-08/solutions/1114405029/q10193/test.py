import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10193StyleProblem(unittest.TestCase):
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

    def test_a_1(self):
        self.check_all_versions("1\n", "5")

    def test_a_2(self):
        self.check_all_versions("2\n", "10")

    def test_a_3(self):
        self.check_all_versions("3\n", "13")

    def test_a_5(self):
        self.check_all_versions("5\n", "25")

    def test_a_7(self):
        self.check_all_versions("7\n", "29")

    def test_a_10(self):
        self.check_all_versions("10\n", "31")

    def test_a_25(self):
        self.check_all_versions("25\n", "77")


if __name__ == "__main__":
    unittest.main()