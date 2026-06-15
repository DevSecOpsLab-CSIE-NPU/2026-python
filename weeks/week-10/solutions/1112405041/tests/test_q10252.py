import unittest
import subprocess
import sys
import os

class TestQ10252(unittest.TestCase):
    def run_solve(self, input_str):
        script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "q10252_hand.py")
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
        """測試題目範例：(0,0), (1,1), (2,2)"""
        # N=3, 奇數點，中位數只有一個
        input_data = "1\n3\n0 0\n1 1\n2 2\n"
        output = self.run_solve(input_data)
        # 最小距離和 4 (P=(1,1) -> 2+0+2), 種數 1
        self.assertEqual(output.strip(), "4 1")

    def test_even_points(self):
        """測試偶數個點，可能有多個整數解"""
        # (0,0), (2,2)
        # N=2, x 中位數範圍 [0, 2], y 中位數範圍 [0, 2]
        # x 解有 0,1,2 (3個), y 解有 0,1,2 (3個), 共 9 種
        # 距離和 4
        input_data = "1\n2\n0 0\n2 2\n"
        output = self.run_solve(input_data)
        self.assertEqual(output.strip(), "4 9")

if __name__ == "__main__":
    unittest.main()
