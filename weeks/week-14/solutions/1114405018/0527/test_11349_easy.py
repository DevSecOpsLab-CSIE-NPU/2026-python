"""11349-easy 單元測試：驗證更簡潔的中心對稱判斷程式。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("11349-easy.py")


def run_input(input_text: str) -> str:
    # 用子程序跑正式腳本，模擬線上評測讀 stdin 的方式。
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test11349Easy(unittest.TestCase):
    def test_sample(self) -> None:
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
        self.assertEqual(
            run_input(input_text),
            "\n".join([
                "Test #1: Symmetric.",
                "Test #2: Non-symmetric.",
            ]),
        )

    def test_negative_value(self) -> None:
        input_text = (
            "1\n"
            "N = 2\n"
            "1 -1\n"
            "-1 1\n"
        )
        self.assertEqual(run_input(input_text), "Test #1: Non-symmetric.")


if __name__ == "__main__":
    unittest.main()