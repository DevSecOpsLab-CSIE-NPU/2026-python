import unittest
import io
import sys
from unittest.mock import patch

# 引入被測試的模組 (此處為了簡化，直接將解答函式放入或匯入)
# 我們可以直接定義函式來測試

def process_rgb(r, g, b):
    """
    計算單一像素的 X, Y, Z 值
    """
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z

class Test11063(unittest.TestCase):
    def test_rgb_conversion(self):
        """
        測試 RGB 到 XYZ 的轉換是否正確
        """
        r, g, b = 255, 3, 192
        x, y, z = process_rgb(r, g, b)
        
        # 驗證誤差在 0.0001 之內
        self.assertAlmostEqual(x, 0.5149 * 255 + 0.3244 * 3 + 0.1607 * 192, places=4)
        self.assertAlmostEqual(y, 0.2654 * 255 + 0.6704 * 3 + 0.0642 * 192, places=4)
        self.assertAlmostEqual(z, 0.0248 * 255 + 0.1248 * 3 + 0.8504 * 192, places=4)

if __name__ == '__main__':
    unittest.main()
