"""Week 02 Task 1 - Sequence Clean 單元測試

測試目標：
- 驗證去重（保留第一次出現順序）
- 驗證升冪 / 降冪排序
- 驗證偶數序列的擷取是否正確

說明：
- 本測試預設受測程式名為 task1_sequence_clean.py
- 若尚未建立解答程式，測試會失敗，這是 TDD 的 Red 階段
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


CANDIDATE_FILES = ["task1_sequence_clean.py", "main.py"]


class TestTask1SequenceClean(unittest.TestCase):
    """針對 Task 1 的輸出格式與序列處理邏輯進行驗證。"""

    @classmethod
    def setUpClass(cls) -> None:
        """先找出受測程式檔案，讓測試可以直接用 subprocess 執行。"""
        cls.test_dir = Path(__file__).resolve().parent
        cls.solver_path = None

        for filename in CANDIDATE_FILES:
            candidate = cls.test_dir.parent / filename
            if candidate.exists() and candidate.is_file():
                cls.solver_path = candidate
                break

        if cls.solver_path is None:
            raise FileNotFoundError(
                "找不到 Task 1 解答檔案，請建立 task1_sequence_clean.py。"
            )

    def run_solver(self, input_data: str) -> str:
        """執行受測程式，回傳標準輸出。"""
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
                "Task 1 程式執行失敗。\n"
                f"stdout:\n{proc.stdout}\n"
                f"stderr:\n{proc.stderr}"
            )

        return proc.stdout.rstrip("\n")

    def test_sample_sequence(self) -> None:
        """正常情況：題目範例，應產生四種輸出。"""
        input_data = "5 3 5 2 9 2 8 3 1\n"
        expected = "\n".join(
            [
                "dedupe: 5 3 2 9 8 1",
                "asc: 1 2 2 3 3 5 5 8 9",
                "desc: 9 8 5 5 3 3 2 2 1",
                "evens: 2 2 8",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_single_element(self) -> None:
        """邊界情況：只有一個數字時，去重、排序、偶數都應能處理。"""
        input_data = "7\n"
        expected = "\n".join(
            [
                "dedupe: 7",
                "asc: 7",
                "desc: 7",
                "evens: ",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_duplicates_and_negative_numbers(self) -> None:
        """反例：重複值與負數並存，最容易寫錯去重與排序邏輯。"""
        input_data = "4 -1 4 -1 0 2 2 -4\n"
        expected = "\n".join(
            [
                "dedupe: 4 -1 0 2 -4",
                "asc: -4 -1 -1 0 2 2 4 4",
                "desc: 4 4 2 2 0 -1 -1 -4",
                "evens: 4 4 0 2 2 -4",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
