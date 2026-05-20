"""
Unit tests for Problem 11063（RGB -> XYZ 轉換）

包含數個簡單測試以驗證公式與 process() 輸出格式。
"""
import unittest
from problem_11063 import rgb_to_xyz, process


class Test11063(unittest.TestCase):
    def test_rgb_to_xyz_known(self):
        # 驗證數值計算（使用直接公式計算期望值）
        r, g, b = 255, 3, 192
        x, y, z = rgb_to_xyz(r, g, b)
        self.assertAlmostEqual(x, 0.5149*255 + 0.3244*3 + 0.1607*192, places=7)
        self.assertAlmostEqual(y, 0.2654*255 + 0.6704*3 + 0.0642*192, places=7)
        self.assertAlmostEqual(z, 0.0248*255 + 0.1248*3 + 0.8504*192, places=7)

    def test_process_single_pixel_format(self):
        # 單一像素輸入，檢查輸出行數與最後一行平均值格式
        inp = "1\n255 3 192\n"
        out = process(inp).strip().split('\n')
        self.assertEqual(len(out), 2)
        # 第一行應為三個浮點數值
        parts = out[0].split()
        self.assertEqual(len(parts), 3)
        # 最後一行檢查文字與數值格式
        self.assertTrue(out[1].startswith("The average of Y is "))


if __name__ == '__main__':
    unittest.main()
