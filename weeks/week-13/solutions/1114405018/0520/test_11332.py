"""11332 單元測試：測試鏡子可見性簡易演算法。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("11332.py")


def run_input(inp: str) -> str:
    res = subprocess.run([sys.executable, str(SCRIPT)], input=inp, text=True, capture_output=True, check=True)
    return res.stdout.strip()


class Test11332(unittest.TestCase):
    def test_single_segment(self):
        inp = "1\n5 -5 5 5\n"
        out = run_input(inp)
        self.assertEqual(out, "1")

    def test_two_segments(self):
        inp = "2\n1 1 2 2\n-1 1 -2 2\n"
        out = run_input(inp)
        # both visible on their sides
        self.assertEqual(out, "11")


if __name__ == "__main__":
    unittest.main()
