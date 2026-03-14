"""UVA 490 單元測試（含繁體中文註解）。

測試目標：
1. 驗證標準旋轉案例（HELLO / WORLD）。
2. 驗證長度不一的行是否會正確補空白。
3. 驗證包含行內空白時，空白是否被正確保留。
4. 驗證空輸入情況。

同時檢查兩個版本：
- uva490.py
- uva490-easy.py
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS = [BASE_DIR / "uva490.py", BASE_DIR / "uva490-easy.py"]


def run_script(script_path: Path, input_text: str) -> str:
    """以子行程執行指定腳本，回傳標準輸出。"""
    completed = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )

    if completed.returncode != 0:
        raise AssertionError(
            f"腳本執行失敗: {script_path.name}\n"
            f"returncode={completed.returncode}\n"
            f"stderr={completed.stderr}"
        )

    return completed.stdout


class TestUVA490(unittest.TestCase):
    """針對 UVA 490 的核心行為做測試。"""

    def assert_all_scripts(self, input_text: str, expected_output: str) -> None:
        """同一份測資同時驗證兩個版本，確保結果一致。"""
        for script in SCRIPTS:
            with self.subTest(script=script.name):
                actual_output = run_script(script, input_text)
                self.assertEqual(actual_output, expected_output)

    def test_basic_hello_world(self) -> None:
        """基本案例：兩行同長文字旋轉。"""
        input_text = "HELLO\nWORLD\n"
        expected_output = "WH\nOE\nRL\nLL\nDO\n"
        self.assert_all_scripts(input_text, expected_output)

    def test_uneven_line_lengths(self) -> None:
        """長度不一致案例：驗證補空白後旋轉。"""
        input_text = "ROTATE\nME\nPLEASE\n"
        expected_output = "PMR\nLEO\nE T\nA A\nS T\nE E\n"
        self.assert_all_scripts(input_text, expected_output)

    def test_internal_spaces_preserved(self) -> None:
        """驗證行內空白與補空白是否被正確保留。"""
        input_text = "A B\nC\n"
        expected_output = "CA\n  \n B\n"
        self.assert_all_scripts(input_text, expected_output)

    def test_empty_input(self) -> None:
        """空輸入應輸出空字串。"""
        input_text = ""
        expected_output = ""
        self.assert_all_scripts(input_text, expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)