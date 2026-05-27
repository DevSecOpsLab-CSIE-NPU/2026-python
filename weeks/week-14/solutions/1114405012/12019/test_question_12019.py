import subprocess
import sys
import textwrap
import unittest
from pathlib import Path


# 黑箱測試：直接執行同資料夾中的 solution.py。
BASE_DIR = Path(__file__).resolve().parent
TARGET_SCRIPT = BASE_DIR / "solution_12019.py"


class TestQuestion12019(unittest.TestCase):
    # 共用執行器，負責收集標準輸出。
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

    # 以 doomsday 當天、隔一天、月底日期來確認星期偏移是否正確。
    def test_weekday_offsets(self) -> None:
        input_data = textwrap.dedent(
            """\
            5
            1 10
            1 11
            2 29
            3 1
            12 31
            """
        )
        expected = "Tuesday\nWednesday\nWednesday\nThursday\nMonday"
        self.assertEqual(self.run_program(input_data), expected)

    # 再補一組日期，確認同一個月內的偏移可正常運作。
    def test_mid_month_dates(self) -> None:
        input_data = textwrap.dedent(
            """\
            3
            4 4
            4 5
            4 10
            """
        )
        expected = "Wednesday\nThursday\nTuesday"
        self.assertEqual(self.run_program(input_data), expected)


if __name__ == "__main__":
    unittest.main()
