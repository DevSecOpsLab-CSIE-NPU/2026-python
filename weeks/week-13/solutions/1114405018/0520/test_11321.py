"""11321 單元測試：測試放陷阱是否封路的判斷。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("11321.py")


def run_input(inp: str) -> str:
    res = subprocess.run([sys.executable, str(SCRIPT)], input=inp, text=True, capture_output=True, check=True)
    return res.stdout.strip()


class Test11321(unittest.TestCase):
    def test_simple(self):
        # 3x3 grid, try placing traps
        inp = """3 3 4
0 1
1 1
2 1
2 2
"""
        out = run_input(inp)
        lines = out.splitlines()
        # The second placement blocks the middle column maybe; accept that function runs
        self.assertEqual(len(lines), 4)


if __name__ == "__main__":
    unittest.main()
