"""11417 單元測試：驗證 GCD 總和計算。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("11417.py")


def run_input(input_text: str) -> str:
    # 直接模擬線上評測的 stdin / stdout 行為。
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test11417(unittest.TestCase):
    def test_sample(self) -> None:
        input_text = "10\n100\n500\n0\n"
        self.assertEqual(run_input(input_text), "\n".join(["67", "13015", "442011"]))

    def test_small_values(self) -> None:
        # 方便人工心算的小測資，確認基本邏輯沒有錯。
        input_text = "2\n3\n0\n"
        self.assertEqual(run_input(input_text), "1\n3")


if __name__ == "__main__":
    unittest.main()