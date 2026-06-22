"""Stage 5 — 安全性自掃測試

依據 OpenSSF Secure Coding Guide for Python 相關章節，測試安全實踐。
"""

import unittest
import json
import os
from search import binary_search
from benchmark import make_data
from plot import load_results


class TestSecurity(unittest.TestCase):
    """安全性自掃測試"""

    def setUp(self):
        """確保必要檔案存在"""
        self.assertTrue(os.path.exists("results.json"), "請先執行 benchmark.py")
        self.assertTrue(os.path.exists("assets/radar.png"), "請先執行 plot.py")

    def test_make_data_rejects_invalid_input(self):
        """benchmark.make_data 應拒絕負數輸入"""
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_make_data_returns_valid_data(self):
        """benchmark.make_data 應返回有效數據"""
        result = make_data(10)
        self.assertEqual(len(result), 10)
        self.assertTrue(all(0 <= x < 10 for x in result))

    def test_plot_loads_json_correctly(self):
        """plot.load_results 應正確讀取 JSON 文件"""
        results = load_results()
        self.assertIn("results", results)
        self.assertIsInstance(results["results"], list)

    def test_binary_search_documented(self):
        """binary_search 應在 docstring 中說明對未排序輸入的行為"""
        doc = binary_search.__doc__
        self.assertIsNotNone(doc)
        self.assertTrue('未排序' in doc or 'unsorted' in doc)

    def test_no_hardcoded_secrets(self):
        """檢查程式碼中沒有硬編碼密鑰"""
        import timing, search, benchmark, plot

        for mod in [timing, search, benchmark, plot]:
            source = open(mod.__file__).read().lower()
            for sensitive in ['password', 'secret', 'api_key', 'token', 'private_key', 'pwd']:
                self.assertNotIn(sensitive, source, f"{mod.__name__} 疑似包含硬編碼密碼")


if __name__ == "__main__":
    unittest.main()
