"""
測試程式：UVA 11461 — Square Numbers
用 subprocess 直接執行手打版 11461.py，驗證標準輸出是否正確
"""
import unittest
import subprocess
import sys
import os

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '11461.py')


def run(input_text):
    """執行手打版程式，傳入模擬標準輸入，回傳標準輸出（已去除首尾空白）"""
    result = subprocess.run(
        [sys.executable, SCRIPT],
        input=input_text,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


class TestSquareNumbers(unittest.TestCase):

    def test_case1(self):
        """[1, 4]：1 和 4 → 共 2 個"""
        self.assertEqual(run("1 4\n0 0\n"), "2")

    def test_case2(self):
        """[1, 10]：1, 4, 9 → 共 3 個"""
        self.assertEqual(run("1 10\n0 0\n"), "3")

    def test_case3(self):
        """[1, 100000]：題目範例，答案為 316"""
        self.assertEqual(run("1 100000\n0 0\n"), "316")

    def test_exact_square(self):
        """[9, 9]：9 本身是完全平方數 → 1"""
        self.assertEqual(run("9 9\n0 0\n"), "1")

    def test_no_square(self):
        """[2, 3]：區間內無完全平方數 → 0"""
        self.assertEqual(run("2 3\n0 0\n"), "0")

    def test_single_1(self):
        """[1, 1]：1 是完全平方數 → 1"""
        self.assertEqual(run("1 1\n0 0\n"), "1")

    def test_start_at_square(self):
        """[4, 16]：4, 9, 16 → 3 個"""
        self.assertEqual(run("4 16\n0 0\n"), "3")

    def test_multiple_inputs(self):
        """題目三個範例一起輸入"""
        inp = "1 4\n1 10\n1 100000\n0 0\n"
        expected = "2\n3\n316"
        self.assertEqual(run(inp), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
