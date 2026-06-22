import unittest
import os
from search_bench import linear_search, binary_search, generate_radar_chart

class TestSearchBench(unittest.TestCase):
    def setUp(self):
        # 準備排序好的測試數列
        self.data = list(range(100))

    def test_linear_search_found(self):
        # 測試線性搜尋：找到目標
        idx, cmp = linear_search(self.data, 35)
        self.assertEqual(idx, 35)
        self.assertEqual(cmp, 36) # 檢查索引 0-35 共 36 次比較

    def test_linear_search_not_found(self):
        # 測試線性搜尋：找不到目標
        idx, cmp = linear_search(self.data, 105)
        self.assertEqual(idx, -1)
        self.assertEqual(cmp, 100) # 比較完整個陣列共 100 次比較

    def test_binary_search_found_135(self):
        # 測試二分搜尋：在 100000 個元素中尋找 135
        large_data = list(range(100000))
        idx, cmp = binary_search(large_data, 135)
        self.assertEqual(idx, 135)
        self.assertEqual(cmp, 15) # 預期 15 次比較

    def test_binary_search_not_found(self):
        # 測試二分搜尋：找不到目標
        idx, cmp = binary_search(self.data, 105)
        self.assertEqual(idx, -1)
        # 0-99 長度 100，折半次數應該是符合 log_2(100) 約 7 次左右
        self.assertTrue(cmp > 0)

    def test_radar_chart_generation(self):
        # 測試雷達圖產生：生成檔案且檔案大小大於 0
        metrics = {
            "speed": [0.1, 9.9],         # 線性 vs 二分
            "simplicity": [9.0, 5.0],    # 線性簡單
            "no_sort_req": [10.0, 1.0],  # 線性不需排序
            "space_eff": [10.0, 10.0],
            "worst_case_cmp": [1.0, 9.9]
        }
        output_dir = "assets"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_path = os.path.join(output_dir, "radar.png")
        
        # 移除舊檔（若存在）
        if os.path.exists(output_path):
            os.remove(output_path)
            
        generate_radar_chart(metrics, output_path)
        
        # 驗證檔案已成功生成且非空
        self.assertTrue(os.path.exists(output_path))
        self.assertTrue(os.path.getsize(output_path) > 0)

if __name__ == '__main__':
    unittest.main()
