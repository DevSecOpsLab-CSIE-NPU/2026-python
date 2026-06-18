# -*- coding: utf-8 -*-
import unittest
import json
import os

class TestSecurity(unittest.TestCase):
    def test_results_json_is_safe(self):
        """驗證使用 json 模組而非 pickle (CWE-502)"""
        with open("benchmark.py", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("import json", content)
            self.assertNotIn("import pickle", content)

    def test_resource_cleanup_with_statement(self):
        """驗證開檔皆有使用 with 語句確保關檔 (OpenSSF 08)"""
        files_to_check = ["benchmark.py", "plot.py"]
        for filename in files_to_check:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
                if "open(" in content:
                    self.assertIn("with open(", content)

if __name__ == "__main__":
    unittest.main()

