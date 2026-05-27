import subprocess
import sys
import textwrap
import unittest
from pathlib import Path


# 這份測試採用黑箱方式，直接執行同資料夾中的 solution.py。
BASE_DIR = Path(__file__).resolve().parent
TARGET_SCRIPT = BASE_DIR / "solution.py"


class TestQuestion11349(unittest.TestCase):
    # 共用的執行器，負責把輸入送進程式，並取得標準輸出。
    def run_program(self, input_data: str) -> str:
        self.assertTrue(
            TARGET_SCRIPT.exists(),
            msg=f"找不到待測程式：{TARGET_SCRIPT}",
        )

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

    # 官方範例：第一組是中心對稱，第二組因為左下角不同而不是對稱矩陣。
    def test_sample_case(self) -> None:
        input_data = textwrap.dedent(
            """\
            2
            N = 3
            5 1 3
            2 0 2
            3 1 5
            N = 3
            5 1 3
            2 0 2
            0 1 5
            """
        )
        expected = "Test #1: Symmetric.\nTest #2: Non-symmetric."
        self.assertEqual(self.run_program(input_data), expected)

    # 單一元素只要不是負數，就一定符合中心對稱。
    def test_single_positive_value(self) -> None:
        input_data = textwrap.dedent(
            """\
            1
            N = 1
            0
            """
        )
        expected = "Test #1: Symmetric."
        self.assertEqual(self.run_program(input_data), expected)

    # 題目要求所有元素都必須是非負數，所以出現負數時一定要判定失敗。
    def test_contains_negative_number(self) -> None:
        input_data = textwrap.dedent(
            """\
            1
            N = 2
            1 -1
            -1 1
            """
        )
        expected = "Test #1: Non-symmetric."
        self.assertEqual(self.run_program(input_data), expected)

    # 這組資料的相對位置數值相同，但中心對稱檢查時仍要逐對比對。
    def test_center_pair_mismatch(self) -> None:
        input_data = textwrap.dedent(
            """\
            1
            N = 3
            7 2 7
            4 9 4
            7 2 8
            """
        )
        expected = "Test #1: Non-symmetric."
        self.assertEqual(self.run_program(input_data), expected)


if __name__ == "__main__":
    unittest.main()
