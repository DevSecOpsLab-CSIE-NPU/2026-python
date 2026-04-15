"""題目 10193（arctan 分解）單元測試

同時驗證正式版與 easy 版。
"""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
PYTHON = "/Library/Developer/CommandLineTools/usr/bin/python3"
MAIN = BASE / "QUESTION-10193.py"
EASY = BASE / "QUESTION-10193-easy.py"


def run_script(script: Path, input_data: str) -> str:
    result = subprocess.run(
        [PYTHON, str(script)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def brute_min_sum(a: int) -> int:
    n = a * a + 1
    best = None
    for x in range(1, n + 1):
        if n % x == 0:
            y = n // x
            val = 2 * a + x + y
            if best is None or val < best:
                best = val
    return best if best is not None else 0


class TestQuestion10193(unittest.TestCase):
    def assert_both(self, inp: str, expected: str) -> None:
        expected = expected.strip()
        self.assertEqual(run_script(MAIN, inp), expected)
        self.assertEqual(run_script(EASY, inp), expected)

    def test_known_values(self) -> None:
        inp = """1
2
3
5
"""
        expected = """5
10
13
25"""
        self.assert_both(inp, expected)

    def test_bruteforce_small(self) -> None:
        values = [4, 6, 7, 8, 9, 10]
        inp = "\n".join(str(v) for v in values) + "\n"
        expected = "\n".join(str(brute_min_sum(v)) for v in values)
        self.assert_both(inp, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
