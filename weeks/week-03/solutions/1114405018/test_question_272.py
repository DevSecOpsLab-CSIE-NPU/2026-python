"""UVA 272（TeX Quoting）單元測試

使用方式：
1. 把你的解答程式放在同一資料夾，檔名建議為下列其中之一：
   - 272.py
   - question_272.py
   - uva272.py
   - main.py
2. 在此資料夾執行：
   python -m unittest -v test_question_272.py

測試策略：
- 以 subprocess 執行受測程式，模擬線上評測的 stdin / stdout 互動。
- 驗證引號成對轉換邏輯：奇數個 " -> ``，偶數個 " -> ''。
- 測試無引號行、多行、多對引號等情境。
- 若找不到受測檔案，會直接失敗並提示可用檔名。
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


# 依序嘗試這些常見檔名，第一個存在的檔案即作為受測程式
CANDIDATE_FILES = ["272.py", "question_272.py", "uva272.py", "main.py"]


class TestUVA272(unittest.TestCase):
    """針對 UVA 272 TeX 引號轉換進行驗證。"""

    @classmethod
    def setUpClass(cls) -> None:
        """在所有測試前先定位受測解答檔案。"""
        cls.test_dir = Path(__file__).resolve().parent
        cls.solver_path = None

        for filename in CANDIDATE_FILES:
            candidate = cls.test_dir / filename
            if candidate.exists() and candidate.is_file():
                cls.solver_path = candidate
                break

        if cls.solver_path is None:
            raise FileNotFoundError(
                "找不到 UVA 272 解答檔案。請在同資料夾放置下列任一檔名："
                + ", ".join(CANDIDATE_FILES)
            )

    def run_solver(self, input_data: str) -> str:
        """執行受測程式，回傳標準輸出（去除尾端空白）。

        設計重點：
        - 使用 sys.executable 確保以目前 Python 環境執行。
        - 若程式非正常結束，會帶出 stdout/stderr 方便除錯。
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

        return proc.stdout.rstrip('\n')

    def test_official_sample(self) -> None:
        """驗證題目常見官方範例輸入輸出。

        題目範例：
        輸入：\"To be or not to be,\" quoth the bard, \"that is the question.\"
        輸出：``To be or not to be,'' quoth the bard, ``that is the question.''
        """
        input_data = '"To be or not to be," quoth the bard, "that is the question."\n'
        expected = '``To be or not to be,\'\' quoth the bard, ``that is the question.\'\''

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_no_quotes(self) -> None:
        """檢查無引號行是否保持不變。"""
        input_data = "Hello world without any quotes\n"
        expected = "Hello world without any quotes"

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_single_pair_quotes(self) -> None:
        """驗證單一引號對的轉換：第一個 \" -> ``，第二個 \" -> ''。"""
        input_data = 'He said "hello" to me\n'
        expected = 'He said ``hello\'\' to me'

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_multiple_pairs_quotes(self) -> None:
        """驗證多引號對的交替轉換邏輯。

        規則：
        - 第 1, 3, 5, ... 個 \" -> ``
        - 第 2, 4, 6, ... 個 \" -> ''
        """
        input_data = '"first" and "second" and "third"\n'
        expected = '``first\'\' and ``second\'\' and ``third\'\''

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_multiple_lines(self) -> None:
        """驗證多行輸入時，引號計數跨行連續進行。

        重點：引號計數是全文統計，不會在每行重置。
        """
        input_data = '"first line"\n"second line"\n'
        expected = '``first line\'\'\n``second line\'\''

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_quote_with_special_chars(self) -> None:
        """驗證引號與特殊字元（符號、數字）混合時的轉換。"""
        input_data = 'Price: "100$" and weight: "50kg"\n'
        expected = 'Price: ``100$\'\' and weight: ``50kg\'\''

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_empty_quotes(self) -> None:
        """驗證空引號對的轉換。"""
        input_data = 'He said "" nothing\n'
        expected = 'He said ``\'\' nothing'

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_consecutive_quotes(self) -> None:
        """驗證連續引號對（\" \"）的轉換。"""
        input_data = '"" "" ""\n'
        expected = '``\'\' ``\'\' ``\'\''

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
