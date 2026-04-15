"""UVA 10222 單元測試

驗證解碼規則（同列向左 1 鍵）與大小寫/空白保留。
"""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
PYTHON = "/Library/Developer/CommandLineTools/usr/bin/python3"
MAIN = BASE / "QUESTION-10222.py"
EASY = BASE / "QUESTION-10222-easy.py"


def run_script(script: Path, input_data: str) -> str:
    result = subprocess.run(
        [PYTHON, str(script)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


class TestQuestion10222(unittest.TestCase):
    def assert_both(self, inp: str, expected: str) -> None:
        self.assertEqual(run_script(MAIN, inp), expected)
        self.assertEqual(run_script(EASY, inp), expected)

    def test_basic_letters(self) -> None:
        self.assert_both("r\n", "e\n")
        self.assert_both("R\n", "E\n")

    def test_mixed_sentence(self) -> None:
        inp = "yjr od;;p\n"
        # y->t, j->h, r->e, o->i, d->s, ;->l, p->o
        expected = "the isllo\n"
        self.assert_both(inp, expected)

    def test_keep_spaces_and_symbols(self) -> None:
        self.assert_both("r t!\n", "e r!\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
