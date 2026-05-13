import subprocess
import sys
from pathlib import Path
import unittest


class TestQuestion10931(unittest.TestCase):
    """UVA 10931 的黑箱測試。"""

    def setUp(self):
        # 預設測試同層的 10931.py。
        self.solution_path = Path(__file__).with_name("10931.py")

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

    def test_single_one(self):
        # 1 的二進位只有一個 1。
        output = self._run_program("1\n0\n")
        self.assertEqual(output, "The parity of 1 is 1 (mod 2).")

    def test_power_of_two(self):
        # 2 的二進位是 10，只有一個 1。
        output = self._run_program("2\n0\n")
        self.assertEqual(output, "The parity of 10 is 1 (mod 2).")

    def test_multiple_ones(self):
        # 10 的二進位是 1010，有兩個 1。
        output = self._run_program("10\n0\n")
        self.assertEqual(output, "The parity of 1010 is 2 (mod 2).")

    def test_odd_parity(self):
        # 21 的二進位是 10101，有三個 1。
        output = self._run_program("21\n0\n")
        self.assertEqual(output, "The parity of 10101 is 3 (mod 2).")

    def test_multiple_inputs(self):
        # 多筆輸入時，輸出順序必須一致。
        output = self._run_program("1\n2\n10\n21\n0\n")
        self.assertEqual(
            output,
            "The parity of 1 is 1 (mod 2).\nThe parity of 10 is 1 (mod 2).\nThe parity of 1010 is 2 (mod 2).\nThe parity of 10101 is 3 (mod 2).",
        )


if __name__ == "__main__":
    unittest.main()