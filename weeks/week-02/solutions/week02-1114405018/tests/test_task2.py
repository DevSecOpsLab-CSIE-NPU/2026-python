"""Week 02 Task 2 - Student Ranking 單元測試

測試目標：
- 驗證多條件排序：score 降冪、age 升冪、name 升冪
- 驗證只輸出前 k 名
- 驗證同分同齡時的字母排序

說明：
- 本測試預設受測程式名為 task2_student_ranking.py
- 若尚未建立解答程式，測試會失敗，這是 TDD 的 Red 階段
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


CANDIDATE_FILES = ["task2_student_ranking.py", "main.py"]


class TestTask2StudentRanking(unittest.TestCase):
    """針對 Task 2 的排序規則與前 k 名輸出進行驗證。"""

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
                "找不到 Task 2 解答檔案，請建立 task2_student_ranking.py。"
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
                "Task 2 程式執行失敗。\n"
                f"stdout:\n{proc.stdout}\n"
                f"stderr:\n{proc.stderr}"
            )

        return proc.stdout.rstrip("\n")

    def test_sample_ranking(self) -> None:
        """正常情況：題目範例，驗證三層排序與前 k 名。"""
        input_data = "\n".join(
            [
                "6 3",
                "amy 88 20",
                "bob 88 19",
                "zoe 92 21",
                "ian 88 19",
                "leo 75 20",
                "eva 92 20",
                "",
            ]
        )
        expected = "\n".join(
            [
                "eva 92 20",
                "zoe 92 21",
                "bob 88 19",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_k_equals_one(self) -> None:
        """邊界情況：只取前 1 名，應只輸出最佳者。"""
        input_data = "\n".join(
            [
                "4 1",
                "a 60 20",
                "b 90 19",
                "c 90 18",
                "d 70 17",
                "",
            ]
        )
        expected = "c 90 18"

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_tie_break_by_name(self) -> None:
        """反例：score 與 age 都相同時，要依 name 字母序排序。"""
        input_data = "\n".join(
            [
                "5 4",
                "zoe 80 20",
                "amy 80 20",
                "bob 80 20",
                "ian 90 19",
                "eva 80 20",
                "",
            ]
        )
        expected = "\n".join(
            [
                "ian 90 19",
                "amy 80 20",
                "bob 80 20",
                "eva 80 20",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
