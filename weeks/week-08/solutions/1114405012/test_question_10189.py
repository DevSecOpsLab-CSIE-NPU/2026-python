"""UVA 10189 單元測試

同時驗證正式版與 easy 版輸出一致，並檢查格式（含空行）。
"""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
PYTHON = "/Library/Developer/CommandLineTools/usr/bin/python3"
MAIN = BASE / "QUESTION-10189.py"
EASY = BASE / "QUESTION-10189-easy.py"


def run_script(script: Path, input_data: str) -> str:
    result = subprocess.run(
        [PYTHON, str(script)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class TestQuestion10189(unittest.TestCase):
    def assert_both(self, inp: str, expected: str) -> None:
        expected = expected.strip()
        self.assertEqual(run_script(MAIN, inp), expected)
        self.assertEqual(run_script(EASY, inp), expected)

    def test_sample(self) -> None:
        inp = """4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
"""
        expected = """Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100"""
        self.assert_both(inp, expected)

    def test_single_cell(self) -> None:
        inp = """1 1
.
0 0
"""
        expected = """Field #1:
0"""
        self.assert_both(inp, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
