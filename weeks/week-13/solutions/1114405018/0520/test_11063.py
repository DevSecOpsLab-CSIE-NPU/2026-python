"""11063 單元測試：測試 RGB->XYZ 轉換與平均 Y 的計算。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("11063.py")


def run_input(inp: str) -> str:
    res = subprocess.run([sys.executable, str(SCRIPT)], input=inp, text=True, capture_output=True, check=True)
    return res.stdout


class Test11063(unittest.TestCase):
    def test_single_pixel(self):
        # n=1, single pixel R=255,G=0,B=0
        inp = "1\n255 0 0\n"
        out = run_input(inp).strip()
        # 計算手動驗證
        x = 0.5149 * 255
        y = 0.2654 * 255
        z = 0.0248 * 255
        expected = f"{x:.4f} {y:.4f} {z:.4f}\nThe average of Y is {y:.4f}"
        self.assertEqual(out, expected)

    def test_two_pixels(self):
        # n=1 with two pixels n=?? Use n=2 with 4 pixels
        inp = "2\n255 0 0 0 255 0 0 0 255 128 128 128\n"
        out = run_input(inp)
        lines = out.strip().splitlines()
        self.assertEqual(len(lines), 5)  # 4 pixels + average


if __name__ == "__main__":
    unittest.main()
