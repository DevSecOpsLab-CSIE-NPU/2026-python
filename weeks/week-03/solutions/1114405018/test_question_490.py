"""UVA 490（Rotating Sentences）單元測試

使用方式：
1. 把你的解答程式放在同一資料夾，檔名建議為下列其中之一：
   - 490.py
   - question_490.py
   - uva490.py
   - main.py
2. 在此資料夾執行：
   python -m unittest -v test_question_490.py

測試策略：
- 以 subprocess 執行受測程式，模擬線上評測的 stdin / stdout。
- 使用參考實作計算「順時針旋轉 90 度」的正確答案。
- 覆蓋等長字串、不等長字串、空白字元、空行、多行等情境。
- 若找不到受測檔案，測試會直接失敗並提示可用檔名。
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


# 依序嘗試這些常見檔名，第一個存在的檔案即作為受測程式
CANDIDATE_FILES = ["490.py", "question_490.py", "uva490.py", "main.py"]


class TestUVA490(unittest.TestCase):
    """針對 UVA 490 文字旋轉規則進行驗證。"""

    @classmethod
    def setUpClass(cls) -> None:
        """在所有測試開始前，定位受測解答檔案。"""
        cls.test_dir = Path(__file__).resolve().parent
        cls.solver_path = None

        for filename in CANDIDATE_FILES:
            p = cls.test_dir / filename
            if p.exists() and p.is_file():
                cls.solver_path = p
                break

        if cls.solver_path is None:
            raise FileNotFoundError(
                "找不到 UVA 490 解答檔案。請在同資料夾放置下列任一檔名："
                + ", ".join(CANDIDATE_FILES)
            )

    def run_solver(self, input_data: str) -> str:
        """執行受測程式，回傳標準輸出（僅移除尾端換行）。"""
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

        # 只移除最末端換行，避免破壞中間空白資訊
        return proc.stdout.rstrip("\n")

    @staticmethod
    def expected_rotate(input_data: str) -> str:
        """參考實作：將輸入文字順時針旋轉 90 度。

        規則：
        - 輸出列數 = 輸入最長行長度。
        - 每一輸出列由「原輸入從下到上」取相同欄位組成。
        - 對每列結果做 rstrip()，避免不必要尾端空白。
        """
        # 保留輸入中的空白內容，只去掉每行結尾的換行符
        lines = input_data.splitlines()
        if not lines:
            return ""

        width = max(len(line) for line in lines)
        out_lines: list[str] = []

        for col in range(width):
            row_chars = []
            for row in range(len(lines) - 1, -1, -1):
                if col < len(lines[row]):
                    row_chars.append(lines[row][col])
                else:
                    row_chars.append(" ")

            out_lines.append("".join(row_chars).rstrip())

        return "\n".join(out_lines)

    def assert_rotation(self, input_data: str) -> None:
        """比對受測程式輸出與參考實作輸出是否一致。"""
        expected = self.expected_rotate(input_data)
        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_two_equal_length_lines(self) -> None:
        """等長兩行：基本旋轉行為。"""
        self.assert_rotation("HELLO\nWORLD\n")

    def test_single_line(self) -> None:
        """單行輸入：旋轉後會變成每字一行。"""
        self.assert_rotation("Python\n")

    def test_varied_lengths(self) -> None:
        """不等長行：需要空白補齊矩形後再旋轉。"""
        self.assert_rotation("ABC\nDE\nF\n")

    def test_with_internal_spaces(self) -> None:
        """包含行內空白：空白也必須視為一般字元參與旋轉。"""
        self.assert_rotation("A B\nCD E\nF\n")

    def test_contains_empty_line(self) -> None:
        """含空行：空行仍是有效輸入行，旋轉時要正確處理。"""
        self.assert_rotation("AB\n\nC\n")

    def test_punctuation_and_digits(self) -> None:
        """標點與數字：確認各種合法字元都可被正確旋轉。"""
        self.assert_rotation("1,2,3\nA!\nxyz?\n")

    def test_longer_case(self) -> None:
        """較長混合測資：避免僅在小樣本才正確。"""
        self.assert_rotation("rotating\nsentences\nis\nfun!\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
