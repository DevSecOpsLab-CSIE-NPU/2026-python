import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10222DecodeMadMan(unittest.TestCase):
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

        return result.stdout.strip("\n")

    def check_all_versions(self, input_data, expected_output):
        for filename in ["main.py", "main-easy.py", "main-handwritten.py"]:
            actual_output = self.run_program(filename, input_data)
            self.assertEqual(
                actual_output,
                expected_output,
                msg=f"{filename} 輸出錯誤"
            )

    def test_single_letter(self):
        self.check_all_versions("r\n", "e")

    def test_simple_word(self):
        self.check_all_versions("jrw\n", "heq")

    def test_keyboard_neighbors(self):
        self.check_all_versions("yui\n", "tuy")

    def test_digits(self):
        self.check_all_versions("123\n", "`12")

    def test_symbols_and_spaces(self):
        self.check_all_versions("o s, g/\n", "i a. f.")

    def test_multiple_lines(self):
        input_data = "r\n123\njrw\n"
        expected_output = "e\n`12\nheq"
        self.check_all_versions(input_data, expected_output)

    def test_uppercase_input(self):
        self.check_all_versions("R\n", "e")


if __name__ == "__main__":
    unittest.main()