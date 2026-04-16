"""UVA 10019（依題目敘述：Hashmat the Brave Warrior）單元測試

注意：
- 這份題目敘述內容是「輸入兩個整數，輸出兩者差的絕對值」。
- 因此本測試會驗證 |a - b| 的多組輸入輸出行為。

使用方式：
1. 把你的解答程式放在同一資料夾，檔名建議為下列其中之一：
   - 10019.py
   - question_10019.py
   - uva10019.py
   - main.py
2. 在此資料夾執行：
   python -m unittest -v test_question_10019.py

測試策略：
- 以 subprocess 執行受測程式，模擬線上評測 stdin / stdout。
- 驗證多行輸入、數字順序顛倒、零值與大數情境。
- 若找不到受測檔案，測試會直接失敗並提示可用檔名。
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


# 依序嘗試這些常見檔名，第一個存在的檔案即作為受測程式
CANDIDATE_FILES = ["10019.py", "question_10019.py", "uva10019.py", "main.py"]


class TestUVA10019(unittest.TestCase):
    """針對題目中的差值計算規則進行驗證。"""

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
                "找不到 UVA 10019 解答檔案。請在同資料夾放置下列任一檔名："
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
    def expected_for_pairs(pairs: list[tuple[int, int]]) -> str:
        """參考實作：每一行輸出 |a-b|。"""
        return "\n".join(str(abs(a - b)) for a, b in pairs)

    def test_basic_cases(self) -> None:
        """基本範例：一般正整數差值。"""
        pairs = [(10, 12), (20, 20), (100, 99)]
        input_data = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"
        expected = self.expected_for_pairs(pairs)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_reversed_order(self) -> None:
        """順序顛倒時仍應輸出正差值。"""
        pairs = [(1, 100), (100, 1), (999, 1000), (1000, 999)]
        input_data = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"
        expected = self.expected_for_pairs(pairs)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_zero_values(self) -> None:
        """含 0 的情況。"""
        pairs = [(0, 0), (0, 7), (9, 0)]
        input_data = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"
        expected = self.expected_for_pairs(pairs)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_large_values(self) -> None:
        """大數測資（Python int 可直接處理）。"""
        pairs = [
            (2**63 - 1, 0),
            (0, 2**63 - 1),
            (123456789012345678, 123456789012345670),
        ]
        input_data = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"
        expected = self.expected_for_pairs(pairs)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_many_lines(self) -> None:
        """多行連續輸入：逐行對應輸出。"""
        pairs = [(i, i + 3) for i in range(1, 21)]
        input_data = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"
        expected = self.expected_for_pairs(pairs)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
