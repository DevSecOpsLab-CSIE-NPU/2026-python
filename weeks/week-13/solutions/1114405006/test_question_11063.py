"""
單元測試：UVA 11063 — XYZ 色彩轉換

說明：
- 此檔包含一個簡單的轉換函式 `convert_rgb_to_xyz`，以及對該函式的單元測試。
- 所有註解皆為繁體中文，並針對題目要求的輸出格式（四捨五入到小數第四位、每像素一行、最後列印平均 Y）進行驗證。

題目摘錄重點：
- 給定 n*n 個像素，每個像素為三個整數 R G B (0..255)。
- 轉換公式：
  X = 0.5149 * R + 0.3244 * G + 0.1607 * B
  Y = 0.2654 * R + 0.6704 * G + 0.0642 * B
  Z = 0.0248 * R + 0.1248 * G + 0.8504 * B
- 輸出每個像素的 X Y Z（到小數第 4 位），最後輸出 "The average of Y is <avg>"，平均 Y 也到第 4 位。

本測試檔不依賴其他模組，可以直接以 unittest 執行。
"""

import unittest

from question_11063 import convert_rgb_to_xyz


class TestQuestion11063(unittest.TestCase):
    """測試多個情境：單像素與多像素的格式與平均值計算"""

    def test_single_pixel_example(self):
        """
        使用題目敘述中的範例像素：R=255, G=3, B=192
        驗證輸出 X、Y、Z 與平均 Y（只有一個像素時，平均 Y 即為該像素的 Y）。
        """
        pixels = [(255, 3, 192)]
        out = convert_rgb_to_xyz(pixels)

        # 根據手工計算（或精確浮點計算）所得
        expected_pixel_line = "163.1271 82.0146 169.9752"
        expected_avg_line = "The average of Y is 82.0146"

        self.assertEqual(out[0], expected_pixel_line)
        self.assertEqual(out[1], expected_avg_line)

    def test_two_pixels_average(self):
        """
        測試兩個像素：第一個為題目範例，第二個為黑色 (0,0,0)，
        驗證平均 Y 為 (Y1 + Y2)/2。
        """
        pixels = [(255, 3, 192), (0, 0, 0)]
        out = convert_rgb_to_xyz(pixels)

        # 第二個像素為黑色，XYZ 應該都是 0.0000
        self.assertEqual(out[1], "0.0000 0.0000 0.0000")
        # 檢查最後一行平均 Y
        expected_avg = (82.0146 + 0.0) / 2
        self.assertEqual(out[-1], f"The average of Y is {expected_avg:.4f}")


if __name__ == "__main__":
    # 直接運行此檔會執行 unittest
    unittest.main()
