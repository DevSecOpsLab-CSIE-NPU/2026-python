"""
測試程式：UVA 11417 — GCD
用 subprocess 直接執行手打版 11417.py，驗證標準輸出是否正確
"""
import unittest
import subprocess
import sys
import os

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '11417.py')


def run(input_text):
    """執行手打版程式，傳入模擬標準輸入，回傳標準輸出（已去除首尾空白）"""
    result = subprocess.run(
        [sys.executable, SCRIPT],
        input=input_text,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


class TestGCDSum(unittest.TestCase):

    def test_n10(self):
        """N=10：題目範例，答案為 67"""
        self.assertEqual(run("10\n0\n"), "67")

    def test_n100(self):
        """N=100：題目範例，答案為 13015"""
        self.assertEqual(run("100\n0\n"), "13015")

    def test_n500(self):
        """N=500：題目範例，答案為 442011"""
        self.assertEqual(run("500\n0\n"), "442011")

    def test_n2(self):
        """N=2：只有 gcd(1,2)=1，答案為 1"""
        self.assertEqual(run("2\n0\n"), "1")

    def test_n3(self):
        """N=3：gcd(1,2)+gcd(1,3)+gcd(2,3) = 1+1+1 = 3"""
        self.assertEqual(run("3\n0\n"), "3")

    def test_multiple_inputs(self):
        """多個 N 連續輸入，輸出各自一行"""
        inp = "10\n100\n500\n0\n"
        expected = "67\n13015\n442011"
        self.assertEqual(run(inp), expected)

    def test_zero_terminates(self):
        """N=0 時程式應立即結束（輸出為空）"""
        self.assertEqual(run("0\n"), "")


if __name__ == '__main__':
    unittest.main(verbosity=2)
