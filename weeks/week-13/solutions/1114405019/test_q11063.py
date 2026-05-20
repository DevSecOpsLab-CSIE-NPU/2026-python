import unittest
import subprocess
import sys
import os

class TestRGBToXYZ(unittest.TestCase):
    """
    針對題目 11063 (RGB 轉 XYZ) 的單元測試
    驗證轉換公式與平均值計算是否正確
    """
    
    def run_program(self, input_str):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_dir, "q11063.py")
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

    def test_basic_conversion(self):
        # 測試 1x1 的影像，RGB 為 255 255 255
        # X = 0.5149*255 + 0.3244*255 + 0.1607*255 = 1.0000 * 255 = 255.0000
        # Y = 0.2654*255 + 0.6704*255 + 0.0642*255 = 1.0000 * 255 = 255.0000
        # Z = 0.0248*255 + 0.1248*255 + 0.8504*255 = 1.0000 * 255 = 255.0000
        input_data = "1\n255 255 255\n"
        output = self.run_program(input_data)
        
        # 檢查輸出是否包含轉換後的值與平均值
        self.assertIn("255.0000 255.0000 255.0000", output)
        self.assertIn("The average of Y is 255.0000", output)

if __name__ == "__main__":
    unittest.main()
