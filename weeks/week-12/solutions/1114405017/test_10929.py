import unittest  # 匯入 unittest
import subprocess  # 匯入 subprocess
import sys  # 匯入 sys

class Test10929(unittest.TestCase):  # 測試類
    def run_program(self, input_data):  # 運行程式
        result = subprocess.run(
            [sys.executable, '10929.py'],
            input=input_data,
            text=True,
            capture_output=True,
            cwd=r'C:\Users\User\Desktop\2026-python\weeks\week-12\solutions\1114405017'
        )
        return result.stdout.strip()

    def test_case1(self):  # 測試案例 1
        input_data = "11\n22\n23\n121\n0\n"
        expected = "11 is a multiple of 11.\n22 is a multiple of 11.\n23 is not a multiple of 11.\n121 is a multiple of 11."
        self.assertEqual(self.run_program(input_data), expected)

    def test_case2(self):  # 測試案例 2：單一位數
        input_data = "1\n0\n"
        expected = "1 is not a multiple of 11."
        self.assertEqual(self.run_program(input_data), expected)

    def test_case3(self):  # 測試案例 3：大數
        input_data = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111\n0\n"
        expected = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 is a multiple of 11."
        self.assertEqual(self.run_program(input_data), expected)

if __name__ == '__main__':
    unittest.main()