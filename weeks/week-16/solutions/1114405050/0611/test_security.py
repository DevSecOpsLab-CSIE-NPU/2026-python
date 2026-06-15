import unittest
import ast
import os

class TestSecurityRules(unittest.TestCase):
    def get_ast(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            return ast.parse(f.read())

    def test_benchmark_writes_json_safely(self):
        """
        OpenSSF Chapter 8 (Coding Standards) & Chapter 4 (Neutralization):
        確保 benchmark 存檔時使用 `with open(...)` (context manager) 且用 json.dump
        目前 benchmark.py 已經有使用 with open，所以這條會過。
        但我們驗證是否有使用 pickle (不安全，應該用 json)。
        """
        tree = self.get_ast("benchmark.py")
        uses_pickle = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == "pickle":
                        uses_pickle = True
        self.assertFalse(uses_pickle, "Security Violation: CWE-502, should use json instead of pickle.")

    def test_make_data_handles_negative_size(self):
        """
        OpenSSF Chapter 3 (Numbers) / General Robustness:
        benchmark 的 make_data 如果傳入負數，不應該繼續產生，應該 raise ValueError
        """
        from benchmark import make_data
        with self.assertRaises(ValueError, msg="make_data should raise ValueError for negative size"):
            make_data(-5)

    def test_load_results_handles_missing_file(self):
        """
        OpenSSF Chapter 5 (Exception Handling):
        plot.py 的 load_results 如果讀取不存在的檔案，應該要有合理的防護或丟出明確錯誤
        """
        from plot import load_results
        
        # 建立一個測試用的檔案，然後砍掉
        fake_path = "does_not_exist_999.json"
        if os.path.exists(fake_path):
            os.remove(fake_path)
            
        with self.assertRaises((FileNotFoundError, ValueError), msg="load_results should handle missing file explicitly"):
            load_results(fake_path)

if __name__ == '__main__':
    unittest.main()
