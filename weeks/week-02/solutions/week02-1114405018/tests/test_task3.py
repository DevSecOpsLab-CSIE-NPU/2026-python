"""Week 02 Task 3 - Log Summary 單元測試

測試目標：
- 驗證每位使用者的事件總數統計
- 驗證 top_action 的行為統計
- 驗證空輸入（m = 0）處理
- 驗證總數相同時的姓名排序規則

說明：
- 本測試預設受測程式名為 task3_log_summary.py
- 若尚未建立解答程式，測試會失敗，這是 TDD 的 Red 階段
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


CANDIDATE_FILES = ["task3_log_summary.py", "main.py"]


class TestTask3LogSummary(unittest.TestCase):
    """針對 Task 3 的使用者統計與 action 統計進行驗證。"""

    @classmethod
    def setUpClass(cls) -> None:
        """尋找受測程式檔案。"""
        cls.test_dir = Path(__file__).resolve().parent
        cls.solver_path = None

        for filename in CANDIDATE_FILES:
            candidate = cls.test_dir.parent / filename
            if candidate.exists() and candidate.is_file():
                cls.solver_path = candidate
                break

        if cls.solver_path is None:
            raise FileNotFoundError(
                "找不到 Task 3 解答檔案，請建立 task3_log_summary.py。"
            )

    def run_solver(self, input_data: str) -> str:
        """執行受測程式並回傳標準輸出。"""
        proc = subprocess.run(
            [sys.executable, str(self.solver_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
            cwd=str(self.test_dir.parent),
        )

        if proc.returncode != 0:
            self.fail(
                "Task 3 程式執行失敗。\n"
                f"stdout:\n{proc.stdout}\n"
                f"stderr:\n{proc.stderr}"
            )

        return proc.stdout.rstrip("\n")

    def test_sample_summary(self) -> None:
        """正常情況：題目範例式的統計與排序。"""
        input_data = "\n".join(
            [
                "8",
                "alice login",
                "bob login",
                "alice view",
                "alice logout",
                "bob view",
                "bob view",
                "chris login",
                "bob logout",
                "",
            ]
        )
        expected = "\n".join(
            [
                "bob 4",
                "alice 3",
                "chris 1",
                "top_action: login 3",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_empty_input(self) -> None:
        """邊界情況：m = 0，應可處理空資料。"""
        input_data = "0\n"
        expected = "top_action:  0"

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_tie_break_by_user_name(self) -> None:
        """反例：總事件數相同時，使用者名稱應依字母序排序。"""
        input_data = "\n".join(
            [
                "6",
                "zoe login",
                "amy view",
                "zoe view",
                "amy login",
                "bob logout",
                "bob view",
                "",
            ]
        )
        expected = "\n".join(
            [
                "amy 2",
                "bob 2",
                "zoe 2",
                "top_action: login 2",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
