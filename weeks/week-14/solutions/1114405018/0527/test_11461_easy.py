"""11461-easy 單元測試：驗證 11461 簡潔版程式輸出。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("11461-easy.py")


def run_input(input_text: str) -> str:
    res = subprocess.run([sys.executable, str(SCRIPT)], input=input_text, text=True, capture_output=True, check=True)
    return res.stdout.strip()


class Test11461Easy(unittest.TestCase):
    def test_sample(self) -> None:
        inp = "1 4\n1 10\n1 100000\n0 0\n"
        expect = "\n".join(["2", "3", "316"])
        self.assertEqual(run_input(inp), expect)

    def test_single(self) -> None:
        inp = "9 9\n0 0\n"
        self.assertEqual(run_input(inp), "1")


if __name__ == "__main__":
    unittest.main()
