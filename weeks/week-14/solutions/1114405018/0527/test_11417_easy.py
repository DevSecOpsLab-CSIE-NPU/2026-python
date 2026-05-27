"""11417-easy 單元測試：驗證更簡潔的 GCD 總和程式。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("11417-easy.py")


def run_input(input_text: str) -> str:
    # 直接用子程序跑正式腳本，模擬線上評測的輸入輸出。
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test11417Easy(unittest.TestCase):
    def test_sample(self) -> None:
        input_text = "10\n100\n500\n0\n"
        self.assertEqual(run_input(input_text), "\n".join(["67", "13015", "442011"]))

    def test_small_values(self) -> None:
        # 2 -> gcd(1,2)=1；3 -> gcd(1,2)+gcd(1,3)+gcd(2,3)=3。
        input_text = "2\n3\n0\n"
        self.assertEqual(run_input(input_text), "1\n3")


if __name__ == "__main__":
    unittest.main()