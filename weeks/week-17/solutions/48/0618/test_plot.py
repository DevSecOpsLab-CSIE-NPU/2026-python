"""Stage 4 — 雷達圖輸出測試"""

import unittest
import os

PNG_PATH = os.path.join(os.path.dirname(__file__), "assets", "radar.png")


class TestRadarPlot(unittest.TestCase):

    def test_png_exists_and_nonempty(self):
        self.assertTrue(os.path.exists(PNG_PATH), "radar.png not found")
        self.assertGreater(os.path.getsize(PNG_PATH), 0, "radar.png is empty")


if __name__ == "__main__":
    unittest.main()
