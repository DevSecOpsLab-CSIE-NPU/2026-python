"""week-03 手打程式整合測試。

此測試檔直接執行 q*.hand.py，
驗證你的手打版本是否符合題目範例輸出。
"""

import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).parent


def run_script(script_name: str, input_text: str) -> str:
    """執行指定腳本並回傳標準輸出（去除尾端換行）。"""
    result = subprocess.run(
        [sys.executable, str(BASE_DIR / script_name)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.rstrip("\n")


class TestHandWeek03(unittest.TestCase):
    """五題手打版本的功能測試。"""

    def test_q100_hand(self) -> None:
        src = "\n".join([
            "1 10",
            "100 200",
            "201 210",
            "900 1000",
        ]) + "\n"
        expected = "\n".join([
            "1 10 20",
            "100 200 125",
            "201 210 89",
            "900 1000 174",
        ])
        self.assertEqual(run_script("q100.hand.py", src), expected)

    def test_q118_hand(self) -> None:
        src = "\n".join([
            "5 3",
            "1 1 E",
            "RFRFRFRF",
            "3 2 N",
            "FRRFLLFFRRFLL",
            "0 3 W",
            "LLFFFLFLFL",
        ]) + "\n"
        expected = "\n".join([
            "1 1 E",
            "3 3 N LOST",
            "2 3 S",
        ])
        self.assertEqual(run_script("q118.hand.py", src), expected)

    def test_q272_hand(self) -> None:
        src = '"To be or not to be," quoth the bard, "that is the question."\n'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        self.assertEqual(run_script("q272.hand.py", src), expected)

    def test_q299_hand(self) -> None:
        src = "\n".join([
            "3",
            "3",
            "1 3 2",
            "4",
            "4 3 2 1",
            "2",
            "2 1",
        ]) + "\n"
        expected = "\n".join([
            "Optimal train swapping takes 1 swaps.",
            "Optimal train swapping takes 6 swaps.",
            "Optimal train swapping takes 1 swaps.",
        ])
        self.assertEqual(run_script("q299.hand.py", src), expected)

    def test_q490_hand(self) -> None:
        src = "HELLO\nWORLD\n"
        expected = "\n".join([
            "WH",
            "OE",
            "RL",
            "LL",
            "DO",
        ])
        self.assertEqual(run_script("q490.hand.py", src), expected)


if __name__ == "__main__":
    unittest.main()
