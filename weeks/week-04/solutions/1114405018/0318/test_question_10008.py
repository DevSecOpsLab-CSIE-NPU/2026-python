"""UVA 10008（What's Cryptanalysis?）單元測試

使用方式：
1. 把你的解答程式放在同一資料夾，檔名建議為下列其中之一：
   - 10008.py
   - question_10008.py
   - uva10008.py
   - main.py
2. 在此資料夾執行：
   python -m unittest -v test_question_10008.py

測試策略：
- 以 subprocess 執行受測程式，模擬線上評測的 stdin / stdout。
- 驗證大小寫合併統計、忽略非英文字母、以及排序規則。
- 排序規則：先依次數遞減，再依字母遞增。
- 若找不到受測檔案，測試會直接失敗並提示可用檔名。
"""

from __future__ import annotations

import string
import subprocess
import sys
import unittest
from pathlib import Path


# 依序嘗試這些常見檔名，第一個存在的檔案即作為受測程式
CANDIDATE_FILES = ["10008.py", "question_10008.py", "uva10008.py", "main.py"]


class TestUVA10008(unittest.TestCase):
    """針對 UVA 10008 字母頻率分析規則進行驗證。"""

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
                "找不到 UVA 10008 解答檔案。請在同資料夾放置下列任一檔名："
                + ", ".join(CANDIDATE_FILES)
            )

    def run_solver(self, input_data: str) -> str:
        """執行受測程式，回傳標準輸出（移除尾端多餘換行）。"""
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
    def expected_output(lines: list[str]) -> str:
        """參考實作：依題目規則統計並輸出字母頻率。"""
        freq = {ch: 0 for ch in string.ascii_uppercase}

        for line in lines:
            for ch in line:
                if ch.isalpha() and ch.upper() in freq:
                    freq[ch.upper()] += 1

        items = [(ch, cnt) for ch, cnt in freq.items() if cnt > 0]
        items.sort(key=lambda x: (-x[1], x[0]))

        return "\n".join(f"{ch} {cnt}" for ch, cnt in items)

    def assert_case(self, lines: list[str]) -> None:
        """以一組輸入行做整體比對。"""
        input_data = str(len(lines)) + "\n" + "\n".join(lines) + "\n"
        expected = self.expected_output(lines)
        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_sample_style_mixed_case(self) -> None:
        """大小寫混合：A 與 a 應合併計算。"""
        self.assert_case([
            "This is a test.",
            "Count me In!",
            "AaBbCc",
        ])

    def test_ignore_non_letters(self) -> None:
        """非英文字母（數字、符號、空白）不應被統計。"""
        self.assert_case([
            "12345 !!! ???",
            "--__--",
            "A1B2C3",
        ])

    def test_tie_break_by_alphabet(self) -> None:
        """次數相同時應按字母順序（A~Z）輸出。"""
        self.assert_case([
            "bbAA",
            "cC",
            "aB",
        ])

    def test_empty_lines(self) -> None:
        """輸入行可能為空字串，程式仍應正確處理。"""
        self.assert_case([
            "",
            "",
            "Zz",
            "",
        ])

    def test_all_letters_once(self) -> None:
        """A~Z 各一次：輸出次數皆為 1，且按字母順序。"""
        self.assert_case([
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        ])

    def test_no_letters_output_empty(self) -> None:
        """若完全沒有英文字母，輸出應為空。"""
        self.assert_case([
            "123",
            "!@#",
        ])


if __name__ == "__main__":
    unittest.main(verbosity=2)
