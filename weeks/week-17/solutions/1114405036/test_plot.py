
"""Stage 4 — 繪圖輸出測試（最小限度）。
 
只驗證：跑完 make_radar 後 PNG 確實產生且不是空檔。內容（用哪些維度、怎麼
畫）由作者決定，測試不綁死。
"""
 
import json
import unittest
from pathlib import Path
 
import plot
 
 
class TestRadarOutput(unittest.TestCase):
    def test_png_produced_and_non_empty(self):
        with open(plot.RESULTS_PATH, encoding="utf-8") as f:
            report = json.load(f)
 
        output = Path(plot.OUTPUT_PATH)
        if output.exists():
            output.unlink()
 
        returned = plot.make_radar(report, output)
 
        self.assertTrue(output.exists(), "radar.png 應該被產生")
        self.assertGreater(output.stat().st_size, 0, "radar.png 不應是空檔")
        self.assertEqual(Path(returned), output)
 
 
if __name__ == "__main__":
    unittest.main()