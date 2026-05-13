import unittest  # 匯入 unittest
import subprocess  # 匯入 subprocess
import sys  # 匯入 sys

class Test10931(unittest.TestCase):  # 測試類
    def run_program(self, input_data):  # 運行程式
        result = subprocess.run(
            [sys.executable, '10931.py'],
            input=input_data,
            text=True,
            capture_output=True,
            cwd=r'C:\Users\User\Desktop\2026-python\weeks\week-12\solutions\1114405017'
        )
        return result.stdout.strip()

    def test_case1(self):  # 測試案例 1：題目範例
        input_data = "1\n2\n10\n21\n0\n"
        expected = "The parity of 1 is 1 (mod 2).\nThe parity of 10 is 1 (mod 2).\nThe parity of 1010 is 2 (mod 2).\nThe parity of 10101 is 3 (mod 2)."
        self.assertEqual(self.run_program(input_data), expected)

    def test_case2(self):  # 測試案例 2：0 結束
        input_data = "0\n"
        expected = ""
        self.assertEqual(self.run_program(input_data), expected)

    def test_case3(self):  # 測試案例 3：大數
        input_data = "2147483647\n0\n"
        expected = "The parity of 1111111111111111111111111111111 is 31 (mod 2)."
        self.assertEqual(self.run_program(input_data), expected)

if __name__ == '__main__':
    unittest.main()