import subprocess
import sys
import unittest


class TestDigitRootBaseProgram(unittest.TestCase):
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

    def test_sample_case_outputs_digit_roots_for_multiple_numbers(self):
        input_text = "0\n8\n63\n"
        expected = "0\n2\n1\n"
        self.assertEqual(self.run_program(input_text), expected)

    def test_edge_case_zero_outputs_zero(self):
        input_text = "0\n"
        expected = "0\n"
        self.assertEqual(self.run_program(input_text), expected)

    def test_multi_round_case_reduces_until_one_base_3_digit(self):
        input_text = "63\n"
        expected = "1\n"
        self.assertEqual(self.run_program(input_text), expected)


if __name__ == "__main__":
    unittest.main()
