"""Stage 4 — 繪圖輸出測試

規格:plot.py 的 load_results / plot_results 必須
  1. 讀 results.json 成功
  2. 輸出 assets/benchmark.png 並且非空檔
  3. plot.py 開頭加 matplotlib.use("Agg") 才能在無視窗環境跑

AI 提示詞:
- 需要測試繪圖函式是否正確地讀取 results.json
- 需要驗證繪圖函式是否正確地生成 PNG 檔案
- 需要確保圖表的視覺化效果符合要求（log 軸、標籤等）
"""

import unittest
import os
from plot import load_results, plot_results


class TestPlotFunctions(unittest.TestCase):
    def setUp(self):
        """設置測試環境"""
        self.results_path = "results.json"
        self.output_path = "assets/benchmark.png"
        
        # 確保 assets 目錄存在
        os.makedirs("assets", exist_ok=True)
    
    def test_load_results(self):
        """測試 load_results 函式是否正確讀取 results.json"""
        results = load_results(self.results_path)
        
        # 驗證結果結構
        self.assertIsInstance(results, dict)
        self.assertIn("500", results)
        self.assertIn("1000", results)
        self.assertIn("2000", results)
        self.assertIn("4000", results)
        
        # 驗證每個數據規模的結構
        for size, size_results in results.items():
            self.assertIsInstance(size_results, dict)
            self.assertIn("bubble", size_results)
            self.assertIn("quick", size_results)
            self.assertIn("merge", size_results)
            self.assertIn("bubble_fast", size_results)
            self.assertIn("quick_fast", size_results)
            self.assertIn("merge_fast", size_results)
            self.assertIn("baseline", size_results)
            
            # 驗證每個演算法的結構
            for sort_name, stats in size_results.items():
                self.assertIsInstance(stats, dict)
                self.assertIn("times", stats)
                self.assertIn("average", stats)
                self.assertIn("min", stats)
                self.assertIn("max", stats)
                self.assertIsInstance(stats["times"], list)
                self.assertIsInstance(stats["average"], float)
                self.assertIsInstance(stats["min"], float)
                self.assertIsInstance(stats["max"], float)
    
    def test_plot_results_generates_file(self):
        """測試 plot_results 是否生成 PNG 檔案"""
        # 確保 results.json 存在
        self.assertTrue(os.path.exists(self.results_path))
        
        # 載入結果
        results = load_results(self.results_path)
        
        # 繪製圖表
        plot_results(results, self.output_path)
        
        # 驗證檔案是否存在
        self.assertTrue(os.path.exists(self.output_path))
        
        # 驗證檔案大小不為空
        file_size = os.path.getsize(self.output_path)
        self.assertGreater(file_size, 0)
    
    def test_plot_results_with_empty_data(self):
        """測試 plot_results 是否能處理空數據"""
        empty_results = {}
        
        # 應該不會崩潰
        plot_results(empty_results, self.output_path)
        
        # 驗證檔案是否存在
        self.assertTrue(os.path.exists(self.output_path))
        
        # 驗證檔案大小不為空
        file_size = os.path.getsize(self.output_path)
        self.assertGreater(file_size, 0)


if __name__ == "__main__":
    unittest.main()