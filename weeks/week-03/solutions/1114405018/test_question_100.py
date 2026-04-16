"""UVA 100（3n+1）單元測試

使用方式：
1. 把你的解答程式放在同一資料夾，檔名建議為下列其中之一：
   - 100.py
   - question_100.py
   - uva100.py
   - main.py
2. 在此資料夾執行：
   python -m unittest -v test_question_100.py

說明：
- 本測試會以 subprocess 執行你的程式，餵入標準輸入並比對標準輸出。
- 若找不到解答檔案，測試會直接失敗並提示可用檔名。
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


# 可接受的解答檔名（依序搜尋）
CANDIDATE_FILES = ["100.py", "question_100.py", "uva100.py", "main.py"]


class TestUVA100(unittest.TestCase):
    """針對 UVA 100 題目的核心行為驗證。"""

    @classmethod
    def setUpClass(cls) -> None:
        """在測試開始前，定位受測解答檔案。"""
        cls.test_dir = Path(__file__).resolve().parent
        cls.solver_path = None

        for filename in CANDIDATE_FILES:
            p = cls.test_dir / filename
            if p.exists() and p.is_file():
                cls.solver_path = p
                break

        if cls.solver_path is None:
            raise FileNotFoundError(
                "找不到解答檔案。請在同資料夾放置下列任一檔名："
                + ", ".join(CANDIDATE_FILES)
            )

    @staticmethod
    def cycle_length(n: int) -> int:
        """參考實作：計算單一 n 的 cycle-length（含起點與終點 1）。"""
        length = 1
        while n != 1:
            if n % 2 == 1:
                n = 3 * n + 1
            else:
                n //= 2
            length += 1
        return length

    @classmethod
    def expected_max_cycle(cls, i: int, j: int) -> int:
        """參考實作：計算區間 [min(i,j), max(i,j)] 的最大 cycle-length。"""
        lo, hi = min(i, j), max(i, j)
        best = 0
        for n in range(lo, hi + 1):
            best = max(best, cls.cycle_length(n))
        return best

    def run_solver(self, input_data: str) -> str:
        """執行受測程式，回傳標準輸出（去除尾端空白）。"""
        proc = subprocess.run(
            [sys.executable, str(self.solver_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
            cwd=str(self.test_dir),
        )

        # 若程式異常退出，回報 stderr 便於除錯
        if proc.returncode != 0:
            self.fail(
                "受測程式執行失敗（return code != 0）。\n"
                f"stdout:\n{proc.stdout}\n"
                f"stderr:\n{proc.stderr}"
            )

        return proc.stdout.strip()

    def test_sample_cases(self) -> None:
        """驗證題目常見範例輸入輸出。"""
        input_data = "\n".join(
            [
                "1 10",
                "100 200",
                "201 210",
                "900 1000",
                "",
            ]
        )
        expected = "\n".join(
            [
                "1 10 20",
                "100 200 125",
                "201 210 89",
                "900 1000 174",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_reversed_range_keeps_original_order(self) -> None:
        """當 i > j 時，輸出前兩欄仍應維持原輸入順序。"""
        input_data = "10 1\n"
        actual = self.run_solver(input_data)
        self.assertEqual(actual, "10 1 20")

    def test_single_value_ranges(self) -> None:
        """檢查單點區間（i == j）的正確性。"""
        pairs = [(1, 1), (22, 22), (999, 999)]
        lines = [f"{a} {b}" for a, b in pairs]
        input_data = "\n".join(lines) + "\n"

        expected_lines = []
        for a, b in pairs:
            best = self.expected_max_cycle(a, b)
            expected_lines.append(f"{a} {b} {best}")

        actual = self.run_solver(input_data)
        self.assertEqual(actual, "\n".join(expected_lines))

    def test_multiple_lines_batch(self) -> None:
        """檢查多行輸入是否逐行輸出且行數一致。"""
        pairs = [(5, 10), (30, 25), (77, 88), (123, 321)]
        input_data = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"

        actual = self.run_solver(input_data)
        actual_lines = actual.splitlines()
        self.assertEqual(len(actual_lines), len(pairs))

        expected_lines = []
        for a, b in pairs:
            best = self.expected_max_cycle(a, b)
            expected_lines.append(f"{a} {b} {best}")

        self.assertEqual(actual_lines, expected_lines)

    def test_small_random_like_regression_set(self) -> None:
        """用一組小範圍回歸資料做交叉驗證，防止實作邏輯退化。"""
        pairs = [
            (2, 3),
            (7, 11),
            (15, 19),
            (50, 60),
            (99, 101),
            (871, 879),
        ]
        input_data = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"

        expected_lines = []
        for a, b in pairs:
            expected_lines.append(f"{a} {b} {self.expected_max_cycle(a, b)}")

        actual = self.run_solver(input_data)
        self.assertEqual(actual.splitlines(), expected_lines)


if __name__ == "__main__":
    unittest.main(verbosity=2)
