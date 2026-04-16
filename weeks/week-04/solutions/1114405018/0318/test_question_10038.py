"""UVA 10038（Jolly Jumpers）單元測試

使用方式：
1. 把你的解答程式放在同一資料夾，檔名建議為下列其中之一：
   - 10038.py
   - question_10038.py
   - uva10038.py
   - main.py
2. 在此資料夾執行：
   python -m unittest -v test_question_10038.py

測試策略：
- 以 subprocess 執行受測程式，模擬線上評測 stdin / stdout。
- 驗證 Jolly 判定規則：相鄰差值絕對值需剛好涵蓋 1..n-1。
- 覆蓋 jolly、非 jolly、n=1、含負數、多行輸入等情境。
- 若找不到受測檔案，測試會直接失敗並提示可用檔名。
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


# 依序嘗試這些常見檔名，第一個存在的檔案即作為受測程式
CANDIDATE_FILES = ["10038.py", "question_10038.py", "uva10038.py", "main.py"]


class TestUVA10038(unittest.TestCase):
    """針對 UVA 10038 Jolly Jumpers 規則進行驗證。"""

    @classmethod
    def setUpClass(cls) -> None:
        """在所有測試開始前，先定位受測解答檔案。"""
        cls.test_dir = Path(__file__).resolve().parent
        cls.solver_path = None

        for filename in CANDIDATE_FILES:
            p = cls.test_dir / filename
            if p.exists() and p.is_file():
                cls.solver_path = p
                break

        if cls.solver_path is None:
            raise FileNotFoundError(
                "找不到 UVA 10038 解答檔案。請在同資料夾放置下列任一檔名："
                + ", ".join(CANDIDATE_FILES)
            )

    def run_solver(self, input_data: str) -> str:
        """執行受測程式並回傳標準輸出（去除尾端換行）。"""
        proc = subprocess.run(
            [sys.executable, str(self.solver_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
            cwd=str(self.test_dir),
        )

        if proc.returncode != 0:
            self.fail(
                "受測程式執行失敗（return code != 0）。\n"
                f"stdout:\n{proc.stdout}\n"
                f"stderr:\n{proc.stderr}"
            )

        return proc.stdout.rstrip("\n")

    @staticmethod
    def is_jolly(seq: list[int]) -> bool:
        """參考實作：判斷序列是否為 jolly jumper。"""
        n = len(seq)
        if n <= 1:
            return True

        diffs = {abs(seq[i] - seq[i - 1]) for i in range(1, n)}
        return diffs == set(range(1, n))

    def expected_for_sequences(self, sequences: list[list[int]]) -> str:
        """依序列產生預期輸出。"""
        lines = []
        for seq in sequences:
            lines.append("Jolly" if self.is_jolly(seq) else "Not jolly")
        return "\n".join(lines)

    def test_given_style_examples(self) -> None:
        """題目常見範例型態：一個 jolly、一個非 jolly。"""
        sequences = [
            [1, 4, 2, 3],
            [1, 4, 2, -1, 6],
        ]
        input_data = "\n".join(
            [
                "4 1 4 2 3",
                "5 1 4 2 -1 6",
                "",
            ]
        )
        expected = self.expected_for_sequences(sequences)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_single_number_sequence(self) -> None:
        """n=1 時沒有差值需求，應視為 Jolly。"""
        sequences = [[100]]
        input_data = "1 100\n"
        expected = self.expected_for_sequences(sequences)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_contains_zero_diff_not_jolly(self) -> None:
        """若相鄰差值出現 0，通常無法涵蓋 1..n-1，應為 Not jolly。"""
        sequences = [[5, 5, 6]]
        input_data = "3 5 5 6\n"
        expected = self.expected_for_sequences(sequences)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_negative_values(self) -> None:
        """含負數也應正確判斷。"""
        sequences = [
            [-1, -4, -2, -3],
            [0, -3, -1, -4],
        ]
        input_data = "\n".join(
            [
                "4 -1 -4 -2 -3",
                "4 0 -3 -1 -4",
                "",
            ]
        )
        expected = self.expected_for_sequences(sequences)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_multiple_lines_mixed(self) -> None:
        """多行混合測資：逐行輸出對應結果。"""
        sequences = [
            [2, 1],          # diff={1} => Jolly
            [1, 3, 5],       # diff={2,2} => Not jolly (缺 1)
            [10, 7, 5, 8],   # diff={3,2,3} => Not jolly (缺 1)
            [4, 2, 3, 1],    # diff={2,1,2} => Not jolly (缺 3)
        ]
        input_data = "\n".join(
            [
                "2 2 1",
                "3 1 3 5",
                "4 10 7 5 8",
                "4 4 2 3 1",
                "",
            ]
        )
        expected = self.expected_for_sequences(sequences)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
