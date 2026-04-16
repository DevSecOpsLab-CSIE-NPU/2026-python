"""UVA 948（Find the Fake Coin）單元測試

使用方式：
1. 把你的解答程式放在同一資料夾，檔名建議為下列其中之一：
   - 948.py
   - question_948.py
   - uva948.py
   - main.py
2. 在此資料夾執行：
   python -m unittest -v test_question_948.py

測試策略：
- 以 subprocess 執行受測程式，模擬線上評測的 stdin / stdout。
- 驗證「唯一假幣」與「無法唯一判斷輸出 0」兩種情況。
- 驗證多組測資之間的空白行格式。
- 若找不到受測檔案，測試會直接失敗並提示可用檔名。
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


# 依序嘗試這些常見檔名，第一個存在的檔案即作為受測程式
CANDIDATE_FILES = ["948.py", "question_948.py", "uva948.py", "main.py"]


class TestUVA948(unittest.TestCase):
    """針對 UVA 948 假幣判定邏輯進行驗證。"""

    @classmethod
    def setUpClass(cls) -> None:
        """在所有測試開始前，先定位受測解答檔案。"""
        cls.test_dir = Path(__file__).resolve().parent
        cls.solver_path = None

        for filename in CANDIDATE_FILES:
            candidate = cls.test_dir / filename
            if candidate.exists() and candidate.is_file():
                cls.solver_path = candidate
                break

        if cls.solver_path is None:
            raise FileNotFoundError(
                "找不到 UVA 948 解答檔案。請在同資料夾放置下列任一檔名："
                + ", ".join(CANDIDATE_FILES)
            )

    def run_solver(self, input_data: str) -> str:
        """執行受測程式並回傳標準輸出。

        注意：
        - 這裡只移除尾端多餘換行，不改動中間空白與空行。
        - 若程式執行失敗，會把 stdout / stderr 一併回報，方便除錯。
        """
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

    def test_unique_heavy_coin(self) -> None:
        """驗證可以找出「唯一較重」的假幣。"""
        # 3 個硬幣，兩次秤重：
        # 1) 1 vs 2 =，代表 1 與 2 都是真的
        # 2) 3 vs 1 >，代表 3 比真幣重，因此 3 是假幣
        input_data = "\n".join(
            [
                "1",
                "3 2",
                "1 1 2",
                "=",
                "1 3 1",
                ">",
                "",
            ]
        )
        expected = "3"

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_unique_light_coin(self) -> None:
        """驗證可以找出「唯一較輕」的假幣。"""
        # 3 個硬幣，兩次秤重：
        # 1) 1 vs 3 =，代表 1 與 3 都是真的
        # 2) 2 vs 1 <，代表 2 比真幣輕，因此 2 是假幣
        input_data = "\n".join(
            [
                "1",
                "3 2",
                "1 1 3",
                "=",
                "1 2 1",
                "<",
                "",
            ]
        )
        expected = "2"

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_ambiguous_returns_zero(self) -> None:
        """當資訊不足以唯一決定假幣時，應輸出 0。"""
        # 這裡只有一次秤重：1 vs 2 =。
        # 3、4 沒有被秤到，因此無法唯一知道到底是哪一枚假幣。
        input_data = "\n".join(
            [
                "1",
                "4 1",
                "1 1 2",
                "=",
                "",
            ]
        )
        expected = "0"

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_multiple_cases_with_blank_lines(self) -> None:
        """驗證多組測資與組間空白行的輸出格式。"""
        # 三組測資，分別對應：
        # 1) 唯一較重的 3
        # 2) 唯一較輕的 2
        # 3) 無法唯一判斷 -> 0
        input_data = "\n".join(
            [
                "3",
                "3 2",
                "1 1 2",
                "=",
                "1 3 1",
                ">",
                "",
                "3 2",
                "1 1 3",
                "=",
                "1 2 1",
                "<",
                "",
                "4 1",
                "1 1 2",
                "=",
                "",
            ]
        )
        expected = "\n".join(
            [
                "3",
                "",
                "2",
                "",
                "0",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
