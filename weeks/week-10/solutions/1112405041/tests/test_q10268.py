import unittest
import subprocess
import sys
import os

class TestQ10268(unittest.TestCase):
    def run_solve(self, input_str):
        script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "q10268_hand.py")
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
        """測試基本案例"""
        # 2 個水球，3 層樓 -> 需要 2 次 (1樓丟，沒破2樓丟；破了1樓丟)
        input_data = "2 3\n0\n"
        output = self.run_solve(input_data)
        self.assertEqual(output.strip(), "2")

    def test_many_balloons(self):
        """測試多水球情況"""
        # 10 個水球，1000 層樓
        # T=10, F(10, 10) = 2^10 - 1 = 1023 >= 1000, 應為 10 次
        input_data = "10 1000\n0\n"
        output = self.run_solve(input_data)
        self.assertEqual(output.strip(), "10")

    def test_more_than_63(self):
        """測試超過 63 次的情況"""
        # 1 個水球，100 層樓
        input_data = "1 100\n0\n"
        output = self.run_solve(input_data)
        self.assertEqual(output.strip(), "More than 63 trials needed.")

if __name__ == "__main__":
    unittest.main()
