import unittest
import subprocess
import sys
import os

class TestMirrors(unittest.TestCase):
    """
    針對題目 11332 (鏡子可見度) 的單元測試
    """
    
    def run_program(self, input_str):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_dir, "q11332.py")
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

    def test_basic_visibility(self):
        # 兩個鏡子
        # 鏡子 1: (1, -1) 到 (1, 1) -> 在前面
        # 鏡子 2: (2, -3) 到 (2, 3) -> 在後面，但比鏡子 1 長，兩端應可見
        input_data = "2\n1 -1 1 1\n2 -3 2 3\n"
        output = self.run_program(input_data)
        self.assertEqual(output, "1 1")

if __name__ == "__main__":
    unittest.main()
