import unittest
import subprocess
import io
import sys
import os

class TestQ10226(unittest.TestCase):
    def run_solve(self, input_str):
        # 取得 q10226_hand.py 的絕對路徑
        script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "q10226_hand.py")

        # 執行程式並獲取輸出
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=input_str)
        return stdout

    def test_sample_case(self):
        """測試題目基本範例"""
        input_data = "3\n0\n0\n0\n"
        output = self.run_solve(input_data)
        # ABC
        #  CB
        # BAC
        #  CA
        # CAB
        #  BA
        lines = output.strip().split('\n')
        self.assertEqual(lines[0], "ABC")
        self.assertEqual(lines[1], " CB")
        self.assertEqual(lines[2], "BAC")

    def test_with_constraints(self):
        """測試帶有限制的案例"""
        # N=2, 第 1 人不想排在位置 1 (所以第 1 人必須在位置 2)
        # A: 1 0
        # B: 0
        input_data = "2\n1 0\n0\n"
        output = self.run_solve(input_data)
        # 排列只有 BA (A在2, B在1)
        # 注意：字典序會先嘗試 AB，但 A 不能在 1，所以只有 BA
        self.assertEqual(output.strip(), "BA")

if __name__ == "__main__":
    unittest.main()
