import subprocess
import sys
from pathlib import Path
import unittest


class TestQuestion10908(unittest.TestCase):
    """UVA 10908 的黑箱測試。

    直接餵標準輸入，確認程式輸出的最大正方形邊長是否正確。
    """

    def setUp(self):
        # 預設測試同層的 10908.py，符合提交時的檔名慣例。
        self.solution_path = Path(__file__).with_name("10908.py")

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

    def test_sample_case(self):
        # 題目範例，確認基本格式與輸出順序。
        output = self._run_program(
            "1\n"
            "7 10 4\n"
            "abbbaaaaaa\n"
            "abbbaaaaaa\n"
            "abbbaaaaaa\n"
            "aaaaaaaaaa\n"
            "aaaaaaaaaa\n"
            "aaccaaaaaa\n"
            "aaccaaaaaa\n"
            "1 2\n"
            "2 4\n"
            "4 6\n"
            "5 2\n"
        )
        self.assertEqual(output, "7 10 4\n3\n1\n5\n1")

    def test_single_cell_grid(self):
        # 只有一個字元時，最大正方形一定是 1。
        output = self._run_program("1\n1 1 1\na\n0 0\n")
        self.assertEqual(output, "1 1 1\n1")

    def test_all_same_small_grid(self):
        # 全部字元相同時，可以一直擴張到邊界允許的最大範圍。
        output = self._run_program("1\n3 3 1\naaa\naaa\naaa\n1 1\n")
        self.assertEqual(output, "3 3 1\n3")

    def test_center_blocked_by_different_char(self):
        # 只要新擴張的範圍中出現不同字元，就要停在前一層。
        output = self._run_program("1\n3 3 1\naaa\naba\naaa\n1 1\n")
        self.assertEqual(output, "3 3 1\n1")

    def test_multiple_queries(self):
        # 同一張圖有多個查詢時，輸出順序必須和查詢順序一致。
        output = self._run_program(
            "1\n"
            "5 5 3\n"
            "aaaaa\n"
            "aaaaa\n"
            "aabaa\n"
            "aaaaa\n"
            "aaaaa\n"
            "2 2\n"
            "0 0\n"
            "4 4\n"
        )
        self.assertEqual(output, "5 5 3\n1\n1\n1")


if __name__ == "__main__":
    unittest.main()