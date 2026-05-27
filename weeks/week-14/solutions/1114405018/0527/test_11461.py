"""11461 單元測試：驗證完全平方數個數。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("11461.py")


def run_input(input_text: str) -> str:
    # 用子程序執行，確認輸出格式與評測一致。
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test11461(unittest.TestCase):
    def test_sample(self) -> None:
        input_text = "1 4\n1 10\n1 100000\n0 0\n"
        self.assertEqual(run_input(input_text), "\n".join(["2", "3", "316"]))

    def test_single_number_square(self) -> None:
        # 區間只包含 9，答案應該是 1。
        input_text = "9 9\n0 0\n"
        self.assertEqual(run_input(input_text), "1")


if __name__ == "__main__":
    unittest.main()