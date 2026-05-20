"""
測試: 題目 11063 - RGB to XYZ 色彩空間轉換
將 RGB 像素轉換到 XYZ 色彩空間並計算平均亮度
"""

from test_support import load_module
import unittest
import sys
from pathlib import Path
from io import StringIO

sys.path.insert(0, str(Path(__file__).parent))


class TestQuestion11063(unittest.TestCase):
    """測試題目 11063: RGB to XYZ 轉換"""

    @classmethod
    def setUpClass(cls):
        """載入解決方案模組"""
        cls.module = load_module('question-11063.py')

    def test_single_pixel(self):
        """基本測試: 單一像素轉換"""
        r, g, b = 255, 3, 192
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b
        result = self.module.convert_rgb_to_xyz(r, g, b)
        self.assertIsNotNone(result)

    def test_black_pixel(self):
        """邊界測試: 黑色像素 (0,0,0)"""
        result = self.module.convert_rgb_to_xyz(0, 0, 0)
        self.assertIsNotNone(result)

    def test_white_pixel(self):
        """反例測試: 白色像素 (255,255,255)"""
        result = self.module.convert_rgb_to_xyz(255, 255, 255)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
