"""Stage 4: 輸出檔案與報告測試"""
import unittest
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


class TestOutputExists(unittest.TestCase):
    def test_task1_png_exists(self):
        self.assertTrue((OUTPUT_DIR / "task1.png").exists())

    def test_task1_png_nonempty(self):
        p = OUTPUT_DIR / "task1.png"
        self.assertGreater(p.stat().st_size, 0)

    def test_task2_png_exists(self):
        self.assertTrue((OUTPUT_DIR / "task2.png").exists())

    def test_task2_png_nonempty(self):
        p = OUTPUT_DIR / "task2.png"
        self.assertGreater(p.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
