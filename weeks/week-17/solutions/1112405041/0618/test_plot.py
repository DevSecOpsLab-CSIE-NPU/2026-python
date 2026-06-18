import unittest
import os


class TestPlot(unittest.TestCase):

    def test_radar_png_exists(self):
        self.assertTrue(os.path.exists("assets/radar.png"),
                        "雷達圖 assets/radar.png 不存在")

    def test_radar_png_not_empty(self):
        size = os.path.getsize("assets/radar.png")
        self.assertGreater(size, 1000,
                           f"radar.png 太小 ({size} bytes)，可能沒內容")
