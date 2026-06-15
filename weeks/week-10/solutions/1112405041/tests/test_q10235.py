import unittest
import subprocess
import sys
import os

class TestQ10235(unittest.TestCase):
    def run_solve(self, input_str):
        script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "q10235_hand.py")
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=input_str)
        return stdout

    def test_small_grid(self):
        """測試 2x2 滿格網格，哈密頓迴路只有 1 種"""
        input_data = "1\n2 2\n11\n11\n"
        output = self.run_solve(input_data)
        self.assertIn("Case 1: 1", output)

    def test_grid_with_obstacle(self):
        """測試帶有障礙物的 3x3 網格"""
        # 3x3 網格，中間是障礙物
        # 1 1 1
        # 1 0 1
        # 1 1 1
        # 只有外圈一個大迴路，共 1 種
        input_data = "1\n3 3\n111\n101\n111\n"
        output = self.run_solve(input_data)
        self.assertIn("Case 1: 1", output)

    def test_impossible_grid(self):
        """測試無法形成哈密頓迴路的網格"""
        # 2x3 網格，但中間有一個格子是 0
        # 1 0 1
        # 1 1 1
        # 無法一筆劃閉合，應為 0
        input_data = "1\n2 3\n101\n111\n"
        output = self.run_solve(input_data)
        self.assertIn("Case 1: 0", output)

if __name__ == "__main__":
    unittest.main()
