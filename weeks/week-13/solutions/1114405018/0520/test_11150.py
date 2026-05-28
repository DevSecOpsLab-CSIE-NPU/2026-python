"""11150 單元測試：測試青蛙過橋的最少踩石子數。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("11150.py")


def run_input(inp: str) -> str:
    res = subprocess.run([sys.executable, str(SCRIPT)], input=inp, text=True, capture_output=True, check=True)
    return res.stdout.strip()


class Test11150(unittest.TestCase):
    def test_sample(self):
        inp = """10
2 3 5
2 3 5 6 7
"""
        out = run_input(inp)
        self.assertEqual(out, "2")

    def test_no_stones(self):
        inp = """10
2 3 0

"""
        out = run_input(inp)
        self.assertEqual(out, "0")


if __name__ == "__main__":
    unittest.main()
