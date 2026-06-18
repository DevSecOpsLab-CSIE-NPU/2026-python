import os
import unittest


class TestPlot(unittest.TestCase):
    def test_radar_png_exists(self):
        self.assertTrue(os.path.exists("assets/radar.png"))

    def test_radar_png_not_empty(self):
        size = os.path.getsize("assets/radar.png")
        self.assertGreater(size, 0)


if __name__ == "__main__":
    unittest.main()
