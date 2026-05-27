"""12019-easy 單元測試：驗證 12019 簡潔版程式。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("12019-easy.py")


def run_input(input_text: str) -> str:
    res = subprocess.run([sys.executable, str(SCRIPT)], input=input_text, text=True, capture_output=True, check=True)
    return res.stdout.strip()


class Test12019Easy(unittest.TestCase):
    def test_sample(self) -> None:
        inp = "3\n1 11\n1 12\n12 12\n"
        expect = "\n".join(["Wednesday", "Thursday", "Wednesday"]) 
        self.assertEqual(run_input(inp), expect)

    def test_leap(self) -> None:
        inp = "2\n2 29\n6 6\n"
        self.assertEqual(run_input(inp), "\n".join(["Wednesday", "Wednesday"]))


if __name__ == "__main__":
    unittest.main()
