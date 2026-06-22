import subprocess
import sys
import unittest


class TestCaesarCipherProgram(unittest.TestCase):
    def run_program(self, input_text):
        result = subprocess.run(
            [sys.executable, "main.py"],
            input=input_text,
            text=True,
            capture_output=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=f"程式應正常結束，但 stderr 是：{result.stderr}",
        )
        return result.stdout

    def test_sample_case_shifts_uppercase_and_lowercase_letters(self):
        input_text = "Hello, NPU!\nabc XYZ\n"
        expected = "Lipps, RTY!\nefg BCD\n"
        self.assertEqual(self.run_program(input_text), expected)

    def test_edge_case_wraps_around_z_and_Z(self):
        input_text = "wxyz WXYZ zZ aA\n"
        expected = "abcd ABCD dD eE\n"
        self.assertEqual(self.run_program(input_text), expected)

    def test_special_case_keeps_non_letters_and_blank_lines(self):
        input_text = "123, !?\n\nTaiwan 2026!\n"
        expected = "123, !?\n\nXemaer 2026!\n"
        self.assertEqual(self.run_program(input_text), expected)


if __name__ == "__main__":
    unittest.main()
