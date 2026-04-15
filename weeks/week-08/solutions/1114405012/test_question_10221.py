"""UVA 10221 單元測試

比較正式版與 easy 版，並驗證角度單位與短弧處理。
"""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
PYTHON = "/Library/Developer/CommandLineTools/usr/bin/python3"
MAIN = BASE / "QUESTION-10221.py"
EASY = BASE / "QUESTION-10221-easy.py"


def run_script(script: Path, input_data: str) -> str:
    result = subprocess.run(
        [PYTHON, str(script)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class TestQuestion10221(unittest.TestCase):
    def assert_both(self, inp: str, expected: str) -> None:
        expected = expected.strip()
        self.assertEqual(run_script(MAIN, inp), expected)
        self.assertEqual(run_script(EASY, inp), expected)

    def test_sample_style(self) -> None:
        inp = """500 30 deg
700 60 min
200 45 deg
"""
        expected = """3633.775503 3592.408346
124.616509 124.614927
5215.043805 5082.035982"""
        self.assert_both(inp, expected)

    def test_short_arc_conversion(self) -> None:
        # 300 度要視為 60 度短弧。
        inp = """0 300 deg
"""
        expected = """6743.952230 6440.000000"""
        self.assert_both(inp, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
