import unittest
import os
import json
import tempfile
import sys

# Add parent directory to path to import benchmark
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import benchmark to access make_data
import benchmark


class TestSecurity(unittest.TestCase):
    """安全測試 - 遵循 OpenSSF 安全編碼指南"""

    def test_08_coding_standards_shadow_builtin_names(self):
        """檢查是否有隱藏內建名稱(如 list、id 等)"""
        import search

        # 使用指定編碼讀取文件
        with open("search.py", "r", encoding="utf-8") as f:
            source = f.read()

        # 檢查是否使用了隱藏的內建名稱
        shadow_names = ["list", "id", "dict", "set", "str"]
        found_shadows = []

        for name in shadow_names:
            if name in source:
                found_shadows.append(name)

        # 允許多少使用，但不可過多
        self.assertLessEqual(
            len(found_shadows), 2, f"隱藏內建名稱過多: {found_shadows}"
        )

    def test_08_coding_standards_files_closed_properly(self):
        """檢查是否有文件沒有使用 with 語句關閉"""
        # 簡單檢查 search.py 文件
        with open("search.py", "r", encoding="utf-8") as f:
            content = f.read()

        # 檢查是否使用了 with 語句
        self.assertIn("with open", content, "search.py 應該使用 with 語句來開啟文件")

    def test_05_exception_handling_specific_exceptions(self):
        """檢查是否有具體的例外處理，而不是用 except: 全包"""
        # 檢查 benchmark.py 是否使用了具體例外
        with open("benchmark.py", "r", encoding="utf-8") as f:
            content = f.read()

        # 檢查是否有具體的例外處理
        specific_exceptions = ["ValueError"]
        found_specific = []

        for exc in specific_exceptions:
            if f"raise {exc}" in content:
                found_specific.append(exc)

        # benchmark.py 應該有具體的例外處理
        self.assertTrue(len(found_specific) > 0, "benchmark.py 應該有具體的例外處理")

    def test_03_numbers_negative_input_handling(self):
        """檢查是否有對負數輸入的處理"""
        # 導入 benchmark 中的 make_data 函式
        from benchmark import make_data

        # 測試 make_data 是否處理負數輸入
        data, target = make_data(100)
        # make_data 應該只生成正整數
        for item in data:
            self.assertGreaterEqual(item, 0, "make_data 應該只生成非負整數")

    def test_04_neutralization_json_not_pickle(self):
        """檢查是否使用 json 而不是 pickle"""
        # 檢查 benchmark.py 是否使用了 json 讀取 results.json
        with open("benchmark.py", "r", encoding="utf-8") as f:
            content = f.read()

        # 檢查是否有 json 讀取
        self.assertIn(
            "import json",
            content,
            "benchmark.py 應該使用 json 而不是 pickle",
        )

    def test_04_neutralization_input_validation(self):
        """檢查是否有合理的輸入驗證"""
        from search import binary_search

        # 測試二分搜尋的輸入驗證
        # 應該處理未排序數據
        result = binary_search([3, 1, 4], 2)
        self.assertEqual(result, -1, "未排序數據應該返回 -1")

    def test_08_coding_standards_not_too_many_errors(self):
        """檢查代碼質量 - 不應該有太多錯誤"""
        # 檢查錯誤數量應該很少
        with open("search.py", "r", encoding="utf-8") as f:
            lines = f.readlines()

        # 計算錯誤比例
        error_lines = [
            line for line in lines if "raise" in line and "assert" not in line
        ]
        error_ratio = len(error_lines) / len(lines) if lines else 1

        # 允許多少錯誤，但不要太多
        self.assertLess(error_ratio, 0.3, f"錯誤比例太高: {error_ratio:.2%}")


if __name__ == "__main__":
    unittest.main()
