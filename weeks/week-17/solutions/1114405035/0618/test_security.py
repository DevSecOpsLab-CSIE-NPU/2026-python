import os
import re
import unittest

from benchmark import make_data


class TestSecurity(unittest.TestCase):
    def test_no_pickle_usage_in_project(self):
        for filename in ["benchmark.py", "plot.py"]:
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                # 檢查是否有未被註解的 import pickle
                has_pickle = re.search(
                    r"^\s*(import pickle|from pickle import)", content, re.MULTILINE
                )
                self.assertIsNone(
                    has_pickle, f"{filename} 安全違規：禁止引入 pickle 模組 (CWE-502)"
                )

    def test_no_assert_for_input_validation_in_timing(self):
        if os.path.exists("timing.py"):
            with open("timing.py", "r", encoding="utf-8") as f:
                content = f.read()
            # 檢查是否有未被註解的 assert 關鍵字
            has_assert = re.search(r"^\s*assert\b", content, re.MULTILINE)
            self.assertIsNone(
                has_assert, "timing.py 安全違規：禁止拿 assert 做輸入驗證 (CWE-703)"
            )

    def test_make_data_rejects_non_positive_integers(self):
        with self.assertRaises(ValueError):
            make_data(0)
        with self.assertRaises(ValueError):
            make_data(-10)


if __name__ == "__main__":
    unittest.main()
