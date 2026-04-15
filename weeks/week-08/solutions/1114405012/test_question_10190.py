"""UVA 10190 單元測試

測試可整除序列與 Boring! 條件。
"""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
PYTHON = "/Library/Developer/CommandLineTools/usr/bin/python3"
MAIN = BASE / "QUESTION-10190.py"
EASY = BASE / "QUESTION-10190-easy.py"


def run_script(script: Path, input_data: str) -> str:
    result = subprocess.run(
        [PYTHON, str(script)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class TestQuestion10190(unittest.TestCase):
    def assert_both(self, inp: str, expected: str) -> None:
        expected = expected.strip()
        self.assertEqual(run_script(MAIN, inp), expected)
        self.assertEqual(run_script(EASY, inp), expected)

    def test_mixed_cases(self) -> None:
        inp = """100 10
27 3
3 2
1 5
59049 3
"""
        expected = """100 10 1
27 9 3 1
Boring!
Boring!
59049 19683 6561 2187 729 243 81 27 9 3 1"""
        self.assert_both(inp, expected)

    def test_equal_values(self) -> None:
        inp = """2 2
"""
        expected = """2 1"""
        self.assert_both(inp, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
