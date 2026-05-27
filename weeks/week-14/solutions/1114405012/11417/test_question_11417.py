import subprocess
import sys
import textwrap
import unittest
from pathlib import Path


# 黑箱測試：直接執行同資料夾中的 solution.py。
BASE_DIR = Path(__file__).resolve().parent
TARGET_SCRIPT = BASE_DIR / "solution_11417.py"


class TestQuestion11417(unittest.TestCase):
    # 共用執行器，負責把輸入送進程式並拿回輸出。
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

    # 官方範例與邊界值混合，確認多組輸入都能正常處理。
    def test_sample_and_small_values(self) -> None:
        input_data = textwrap.dedent(
            """\
            2
            3
            10
            0
            """
        )
        expected = "1\n3\n67"
        self.assertEqual(self.run_program(input_data), expected)

    # 兩個數字時只有一組 pair，答案就是 gcd(1, 2) = 1。
    def test_n_equals_two(self) -> None:
        input_data = textwrap.dedent(
            """\
            2
            0
            """
        )
        expected = "1"
        self.assertEqual(self.run_program(input_data), expected)

    # 再補一個小一點的值，確認總和公式沒有寫錯。
    def test_n_equals_four(self) -> None:
        input_data = textwrap.dedent(
            """\
            4
            0
            """
        )
        expected = "7"
        self.assertEqual(self.run_program(input_data), expected)


if __name__ == "__main__":
    unittest.main()
