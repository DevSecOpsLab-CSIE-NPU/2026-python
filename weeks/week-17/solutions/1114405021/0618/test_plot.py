import unittest
from plot import create_radar_chart, analyze_results
import os
import json


class TestPlot(unittest.TestCase):
    """Plot module tests"""

    def setUp(self):
        """設置測試前的環境"""
        # 創建 results.json 用於測試
        self.test_results = {
            "size_10000": {
                "linear_baseline": 0.001,
                "binary_baseline": 0.0005,
                "linear_v2": 0.002,
                "binary_v2": 0.0003,
                "data_size": 10000,
            },
            "size_50000": {
                "linear_baseline": 0.005,
                "binary_baseline": 0.0025,
                "linear_v2": 0.008,
                "binary_v2": 0.0035,
                "data_size": 50000,
            },
            "size_100000": {
                "linear_baseline": 0.01,
                "binary_baseline": 0.005,
                "linear_v2": 0.02,
                "binary_v2": 0.008,
                "data_size": 100000,
            },
        }

        # 寫入 results.json
        with open("results.json", "w") as f:
            json.dump(self.test_results, f, indent=2)

        # 確保 assets 目錄存在
        os.makedirs("assets", exist_ok=True)

    def tearDown(self):
        """清除測試後的環境"""
        # 刪除 results.json 和 assets/radar.png
        if os.path.exists("results.json"):
            os.remove("results.json")
        if os.path.exists("assets/radar.png"):
            os.remove("assets/radar.png")

    def test_radar_chart_creates_file(self):
        """測試雷達圖是否正確創建 PNG 文件"""
        results = create_radar_chart(self.test_results)
        self.assertTrue(os.path.exists("assets/radar.png"))
        # 檢查文件是否不為空
        self.assertGreater(os.path.getsize("assets/radar.png"), 0)

    def test_analyze_results(self):
        """测试分析函数"""
        analysis = analyze_results(self.test_results)
        self.assertIsNotNone(analysis)
        # 检查是否包含分析内容的关键词
        self.assertIn("Analysis", analysis)
        # 检查是否包含一些预期的内容
        self.assertIn("Speed Trade-off", analysis)

    def test_analyze_results_with_empty_data(self):
        """測試分析空數據的情況"""
        analysis = analyze_results(None)
        self.assertIsNone(analysis)


if __name__ == "__main__":
    unittest.main()
