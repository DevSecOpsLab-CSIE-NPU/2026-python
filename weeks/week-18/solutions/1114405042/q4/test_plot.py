"""Stage 4 — plot.py 雷達圖測試

測試 plot.py 生成的雷達圖是否符合基本要求：
- PNG 確實產生且非空檔
- 圖檔可被讀取
"""

import unittest
import os
import json
from plot import load_results, calculate_dimension_scores, plot_radar_chart


class TestPlot(unittest.TestCase):
    """雷達圖繪製測試"""

    def setUp(self):
        """確保 results.json 存在"""
        self.assertTrue(os.path.exists("results.json"), "results.json 不存在，請先執行 benchmark.py")

    def test_load_results(self):
        """測試 load_results 正確讀取 JSON"""
        results = load_results()
        self.assertIn("results", results)
        self.assertIsInstance(results["results"], list)
        self.assertGreater(len(results["results"]), 0)

    def test_calculate_dimension_scores(self):
        """測試 calculate_dimension_scores 回傳正確結構"""
        results = load_results()
        algorithms, scores = calculate_dimension_scores(results)

        self.assertEqual(algorithms, ["linear_search", "binary_search", "set_search"])

        self.assertEqual(len(scores), 3)
        for algo_scores in scores:
            self.assertEqual(len(algo_scores), 5)
            for score in algo_scores:
                self.assertIsInstance(score, float)
                self.assertTrue(0.0 <= score <= 1.0)

    def test_plot_generates_png(self):
        """測試 plot_radar_chart 生成非空 PNG 檔案"""
        plot_radar_chart(["linear_search", "binary_search", "set_search"], [[0.5]*5]*3)

        self.assertTrue(os.path.exists("assets/radar.png"), "radar.png 未生成")
        self.assertGreater(os.path.getsize("assets/radar.png"), 0, "radar.png 不應為空檔")

    def test_results_json_structure(self):
        """測試 results.json 結構完整"""
        with open("results.json", "r") as f:
            data = json.load(f)

        self.assertIn("results", data)
        for item in data["results"]:
            self.assertIn("n", item)
            self.assertIn("linear", item)
            self.assertIn("binary", item)
            self.assertIn("set", item)

            for algo in ["linear", "binary", "set"]:
                self.assertIn("total_time", item[algo])
                self.assertIn("avg_time", item[algo])
                self.assertIn("records", item[algo])
                self.assertTrue(len(item[algo]["records"]) > 0)


if __name__ == "__main__":
    unittest.main()
