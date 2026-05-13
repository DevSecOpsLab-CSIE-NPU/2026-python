import unittest  # 匯入 unittest 模組
import subprocess  # 匯入 subprocess 模組
import sys  # 匯入 sys 模組

class Test10922(unittest.TestCase):  # 定義測試類
    def run_program(self, input_data):  # 運行程式方法
        result = subprocess.run(
            [sys.executable, '10922.py'],
            input=input_data,
            text=True,
            capture_output=True,
            cwd=r'C:\Users\User\Desktop\2026-python\weeks\week-12\solutions\1114405017'
        )
        return result.stdout.strip()

    def test_case1(self):  # 測試案例 1
        input_data = "9\n18\n27\n99\n10\n0\n"
        expected = "9-degree of 9 is 0.\n9-degree of 18 is 1.\n9-degree of 27 is 1.\n9-degree of 99 is 2.\n10 is not a multiple of 9."
        self.assertEqual(self.run_program(input_data), expected)

    def test_case2(self):  # 測試案例 2：單一位數
        input_data = "1\n0\n"
        expected = "1 is not a multiple of 9."
        self.assertEqual(self.run_program(input_data), expected)

    def test_case3(self):  # 測試案例 3：大數
        input_data = "999999999\n0\n"
        expected = "9-degree of 999999999 is 2."
        self.assertEqual(self.run_program(input_data), expected)

if __name__ == '__main__':
    unittest.main()