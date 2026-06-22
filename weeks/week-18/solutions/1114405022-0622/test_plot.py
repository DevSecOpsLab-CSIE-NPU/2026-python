import unittest
import os
from plot import draw_radar_chart


class TestPlot(unittest.TestCase):

    def test_radar_png_generated(self):
        # 執行繪圖函式
        draw_radar_chart()
        
        # 驗證檔案是否存在
        file_path = "assets/radar.png"
        self.assertTrue(os.path.exists(file_path), f"PNG file {file_path} was not generated")
        
        # 驗證檔案大小不為 0
        self.assertGreater(os.path.getsize(file_path), 0, f"PNG file {file_path} is empty")


if __name__ == "__main__":
    unittest.main()
