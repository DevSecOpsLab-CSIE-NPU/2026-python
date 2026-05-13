import subprocess
import sys
from pathlib import Path
import unittest


class TestQuestion10929(unittest.TestCase):
    """UVA 10929 的黑箱測試。"""

    def setUp(self):
        # 預設測試同層的 10929.py。
        self.solution_path = Path(__file__).with_name("10929.py")

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

    def test_single_multiple(self):
        # 11 本身就是 11 的倍數。
        output = self._run_program("11\n0\n")
        self.assertEqual(output, "11 is a multiple of 11.")

    def test_two_digit_non_multiple(self):
        # 12 不是 11 的倍數。
        output = self._run_program("12\n0\n")
        self.assertEqual(output, "12 is not a multiple of 11.")

    def test_three_digit_multiple(self):
        # 121 是 11 的倍數。
        output = self._run_program("121\n0\n")
        self.assertEqual(output, "121 is a multiple of 11.")

    def test_large_multiple(self):
        # 1001 也是 11 的倍數。
        output = self._run_program("1001\n0\n")
        self.assertEqual(output, "1001 is a multiple of 11.")

    def test_multiple_inputs(self):
        # 同時測多筆資料與結尾 0。
        output = self._run_program("11\n12\n1001\n1234567890\n0\n")
        self.assertEqual(
            output,
            "11 is a multiple of 11.\n12 is not a multiple of 11.\n1001 is a multiple of 11.\n1234567890 is not a multiple of 11.",
        )


if __name__ == "__main__":
    unittest.main()