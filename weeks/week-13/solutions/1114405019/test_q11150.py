import unittest
import subprocess
import sys
import os

class TestFrogJump(unittest.TestCase):
    """
    針對題目 11150 (過河) 的單元測試
    """
    
    def run_program(self, input_str):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_dir, "q11150.py")
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

    def test_sample_case(self):
        # 簡單範例：長度 10, 跳躍 2~3, 1 個石子在位置 5
        # 起點 0, 踩不到 5 的方法：0 -> 3 -> 6 (過橋)
        # 預期最少踩到 0 個
        input_data = "10\n2 3 1\n5\n"
        output = self.run_program(input_data)
        self.assertEqual(output, "0")

if __name__ == "__main__":
    unittest.main()
