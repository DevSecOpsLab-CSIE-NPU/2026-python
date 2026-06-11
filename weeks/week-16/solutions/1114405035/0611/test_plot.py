import unittest
import os
import tempfile
import json
from plot import load_results, plot_results


class TestPlot(unittest.TestCase):
    def setUp(self):
        # 建立一個測試用的臨時 JSON 檔案
        self.test_data = {
            "bubble_sort": {"500": 0.01, "1000": 0.04},
            "quick_sort": {"500": 0.001, "1000": 0.002},
            "merge_sort": {"500": 0.001, "1000": 0.002},
            "quick_sort_optimized": {"500": 0.0008, "1000": 0.0018},
            "builtin_sorted": {"500": 0.0001, "1000": 0.0002}
        }
        self.temp_dir = tempfile.TemporaryDirectory()
        self.json_path = os.path.join(self.temp_dir.name, "test_results.json")
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(self.test_data, f)
            
        self.png_path = os.path.join(self.temp_dir.name, "test_benchmark.png")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_load_results(self):
        # 測試 load_results 可以正確讀取 JSON 並回傳 dict
        loaded = load_results(self.json_path)
        self.assertEqual(loaded, self.test_data)

    def test_plot_results_generates_non_empty_file(self):
        # 測試 plot_results 確實產生 PNG 且檔案不為空
        if os.path.exists(self.png_path):
            os.remove(self.png_path)
            
        plot_results(self.test_data, self.png_path)
        
        self.assertTrue(os.path.exists(self.png_path), "PNG file was not created!")
        self.assertGreater(os.path.getsize(self.png_path), 0, "PNG file is empty!")


if __name__ == "__main__":
    unittest.main()
