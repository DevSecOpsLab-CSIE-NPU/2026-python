import unittest
import subprocess
import sys
import os

class TestTraps(unittest.TestCase):
    """
    針對題目 11321 (陷阱路徑) 的單元測試
    """
    
    def run_program(self, input_str):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_dir, "q11321.py")
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        stdout, stderr = process.communicate(input=input_str)
        return stdout.strip()

    def test_simple_block(self):
        # 3x3 道路，在中間那一列放滿陷阱會封死
        # (0,1), (1,1), (2,1)
        input_data = "3 3 3\n0 1\n1 1\n2 1\n"
        output = self.run_program(input_data)
        # 前兩個應該可以放，最後一個會封死
        expected = "<(_ _)>\n<(_ _)>\n>_<"
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()
