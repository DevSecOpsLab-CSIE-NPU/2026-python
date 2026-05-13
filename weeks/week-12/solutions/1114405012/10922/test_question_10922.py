import subprocess
import sys
from pathlib import Path
import unittest


class TestQuestion10922(unittest.TestCase):
    """UVA 10922 的黑箱測試。"""

    def setUp(self):
        # 預設測試同層的 10922.py。
        self.solution_path = Path(__file__).with_name("10922.py")

    def _run_program(self, raw_input: str) -> str:
        completed = subprocess.run(
            [sys.executable, str(self.solution_path)],
            input=raw_input,
            text=True,
            capture_output=True,
            cwd=self.solution_path.parent,
            check=False,
        )
        return completed.stdout.strip()

    def test_single_nine(self):
        # 9 本身就是 9 的倍數，深度為 1。
        output = self._run_program("9\n0\n")
        self.assertEqual(output, "9-degree of 9 is 1.")

    def test_two_digit_multiple(self):
        # 18 的數字和是 9，所以深度也是 1。
        output = self._run_program("18\n0\n")
        self.assertEqual(output, "9-degree of 18 is 1.")

    def test_depth_two_number(self):
        # 999 需要做兩次數字和才會變成 9。
        output = self._run_program("999\n0\n")
        self.assertEqual(output, "9-degree of 999 is 2.")

    def test_non_multiple(self):
        # 123 不是 9 的倍數。
        output = self._run_program("123\n0\n")
        self.assertEqual(output, "123 is not a multiple of 9.")

    def test_multiple_inputs(self):
        # 同時測多筆輸入，確認輸出順序和格式都正確。
        output = self._run_program("9\n18\n123\n999999999999\n0\n")
        self.assertEqual(
            output,
            "9-degree of 9 is 1.\n9-degree of 18 is 1.\n123 is not a multiple of 9.\n9-degree of 999999999999 is 2.",
        )


if __name__ == "__main__":
    unittest.main()