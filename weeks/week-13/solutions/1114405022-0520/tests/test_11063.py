"""
UVA 11063 — RGB → XYZ 色彩轉換

測試 RGB 轉 XYZ 公式運算與格式化輸出。
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestRGBtoXYZ(unittest.TestCase):
    """測試 UVA 11063：RGB 轉 XYZ 色彩空間"""

    def setUp(self):
        """載入解答模組，若尚未撰寫則跳過"""
        try:
            from solution_11063 import rgb_to_xyz, solve
            self.rgb_to_xyz = rgb_to_xyz
            self.solve = solve
        except ImportError:
            self.skipTest("solution_11063.py 尚未撰寫")

    # ─── 核心公式測試 ────────────────────────────────

    def test_black(self):
        """(R, G, B) = (0, 0, 0) → (0.0, 0.0, 0.0)"""
        x, y, z = self.rgb_to_xyz(0, 0, 0)
        self.assertAlmostEqual(x, 0.0, places=4)
        self.assertAlmostEqual(y, 0.0, places=4)
        self.assertAlmostEqual(z, 0.0, places=4)

    def test_white(self):
        """(R, G, B) = (255, 255, 255) → 計算預期值"""
        x, y, z = self.rgb_to_xyz(255, 255, 255)
        expected_x = 255 * (0.5149 + 0.3244 + 0.1607)
        expected_y = 255 * (0.2654 + 0.6704 + 0.0642)
        expected_z = 255 * (0.0248 + 0.1248 + 0.8504)
        self.assertAlmostEqual(x, expected_x, places=4)
        self.assertAlmostEqual(y, expected_y, places=4)
        self.assertAlmostEqual(z, expected_z, places=4)

    def test_red(self):
        """(R, G, B) = (255, 0, 0) → X 最大"""
        x, y, z = self.rgb_to_xyz(255, 0, 0)
        self.assertAlmostEqual(x, 255 * 0.5149, places=4)
        self.assertAlmostEqual(y, 255 * 0.2654, places=4)
        self.assertAlmostEqual(z, 255 * 0.0248, places=4)

    def test_green(self):
        """(R, G, B) = (0, 255, 0) → Y 最大"""
        x, y, z = self.rgb_to_xyz(0, 255, 0)
        self.assertAlmostEqual(x, 255 * 0.3244, places=4)
        self.assertAlmostEqual(y, 255 * 0.6704, places=4)
        self.assertAlmostEqual(z, 255 * 0.1248, places=4)

    def test_blue(self):
        """(R, G, B) = (0, 0, 255) → Z 最大"""
        x, y, z = self.rgb_to_xyz(0, 0, 255)
        self.assertAlmostEqual(x, 255 * 0.1607, places=4)
        self.assertAlmostEqual(y, 255 * 0.0642, places=4)
        self.assertAlmostEqual(z, 255 * 0.8504, places=4)

    def test_random_values(self):
        """測試題目範例 (255, 3, 192)"""
        x, y, z = self.rgb_to_xyz(255, 3, 192)
        expected_x = 255 * 0.5149 + 3 * 0.3244 + 192 * 0.1607
        expected_y = 255 * 0.2654 + 3 * 0.6704 + 192 * 0.0642
        expected_z = 255 * 0.0248 + 3 * 0.1248 + 192 * 0.8504
        self.assertAlmostEqual(x, expected_x, places=4)
        self.assertAlmostEqual(y, expected_y, places=4)
        self.assertAlmostEqual(z, expected_z, places=4)

    def test_average_y_single_pixel(self):
        """單一像素時，平均 Y 即為該像素 Y"""
        output = self.solve("1\n255 192 3\n")
        lines = [l for l in output.strip().splitlines() if l]
        self.assertIn("The average of Y is", lines[-1])
        # 從輸出中提取 Y 值並四捨五入確認
        pixel_y = 255 * 0.2654 + 192 * 0.6704 + 3 * 0.0642
        expected_y_line = f"The average of Y is {pixel_y:.4f}"
        self.assertEqual(lines[-1], expected_y_line)


if __name__ == '__main__':
    unittest.main()
