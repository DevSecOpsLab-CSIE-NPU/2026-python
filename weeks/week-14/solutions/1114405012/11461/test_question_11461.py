import subprocess
import sys
import textwrap
import unittest
from pathlib import Path


# 黑箱測試：直接執行同資料夾中的 solution.py。
BASE_DIR = Path(__file__).resolve().parent
TARGET_SCRIPT = BASE_DIR / "solution_11461.py"


class TestQuestion11461(unittest.TestCase):
    # 共用執行器，負責送出輸入並收集結果。
    def run_program(self, input_data: str) -> str:
        self.assertTrue(TARGET_SCRIPT.exists(), msg=f"找不到待測程式：{TARGET_SCRIPT}")

        completed = subprocess.run(
            [sys.executable, str(TARGET_SCRIPT)],
            input=input_data,
            text=True,
            capture_output=True,
            cwd=BASE_DIR,
            check=False,
        )

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"程式執行失敗\nSTDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}",
        )
        return completed.stdout.strip()

    # 官方範例與大範圍測資一起確認。
    def test_sample_cases(self) -> None:
        input_data = textwrap.dedent(
            """\
            1 4
            1 10
            1 100000
            0 0
            """
        )
        expected = "2\n3\n316"
        self.assertEqual(self.run_program(input_data), expected)

    # 區間剛好只有一個平方數。
    def test_single_square(self) -> None:
        input_data = textwrap.dedent(
            """\
            4 4
            0 0
            """
        )
        expected = "1"
        self.assertEqual(self.run_program(input_data), expected)

    # 區間裡沒有任何完全平方數。
    def test_no_square(self) -> None:
        input_data = textwrap.dedent(
            """\
            2 3
            0 0
            """
        )
        expected = "0"
        self.assertEqual(self.run_program(input_data), expected)


if __name__ == "__main__":
    unittest.main()
