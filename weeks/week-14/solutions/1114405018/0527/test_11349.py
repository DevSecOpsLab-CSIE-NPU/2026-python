"""11349 單元測試：驗證中心對稱矩陣判斷邏輯。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("11349.py")


def run_input(input_text: str) -> str:
    # 透過子程序執行正式程式，模擬評測系統實際送入資料的方式。
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test11349(unittest.TestCase):
    def test_symmetric_matrix(self) -> None:
        # 中心對稱且全部非負，應判定為 Symmetric。
        input_text = (
            "2\n"
            "N = 3\n"
            "5 1 3\n"
            "2 0 2\n"
            "3 1 5\n"
            "N = 3\n"
            "5 1 3\n"
            "2 0 2\n"
            "0 1 5\n"
        )
        expected = "\n".join([
            "Test #1: Symmetric.",
            "Test #2: Non-symmetric.",
        ])
        self.assertEqual(run_input(input_text), expected)

    def test_negative_value_breaks_rule(self) -> None:
        # 只要出現負數，就算圖形對稱也必須判定為 Non-symmetric。
        input_text = (
            "1\n"
            "N = 2\n"
            "1 -1\n"
            "-1 1\n"
        )
        self.assertEqual(run_input(input_text), "Test #1: Non-symmetric.")

    def test_single_cell_matrix(self) -> None:
        # 1x1 矩陣只要是非負數就符合條件。
        input_text = (
            "1\n"
            "N = 1\n"
            "0\n"
        )
        self.assertEqual(run_input(input_text), "Test #1: Symmetric.")


if __name__ == "__main__":
    unittest.main()