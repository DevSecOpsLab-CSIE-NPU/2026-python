import unittest
import os
import sys

# 將當前目錄加入 path 以便 import 解決
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task1_csv_to_json import filter_by_admission, count_by_dept

class TestTask1(unittest.TestCase):
    def test_filter_keeps_correct_rows(self):
        """測試過濾功能是否正確保留指定的入學方式"""
        rows = [
            {"入學方式": "聯合登記分發", "系所名稱": "資訊工程系"},
            {"入學方式": "甄選入學", "系所名稱": "電機工程系"},
        ]
        result = filter_by_admission(rows, "聯合登記分發")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["系所名稱"], "資訊工程系")

    def test_filter_removes_others(self):
        """測試是否正確排除了非指定的入學方式"""
        rows = [
            {"入學方式": "其他方式", "系所名稱": "測試系"},
        ]
        result = filter_by_admission(rows, "聯合登記分發")
        self.assertEqual(len(result), 0)

    def test_filter_empty_input(self):
        """測試空輸入的情況"""
        self.assertEqual(filter_by_admission([], "聯合登記分發"), [])

    def test_count_by_dept_correct(self):
        """測試系所統計功能"""
        rows = [
            {"系所名稱": "資訊系"},
            {"系所名稱": "資訊系"},
            {"系所名稱": "電機系"},
        ]
        stats = count_by_dept(rows)
        self.assertEqual(stats["資訊系"], 2)
        self.assertEqual(stats["電機系"], 1)

    def test_count_by_dept_empty(self):
        """測試空輸入的統計"""
        self.assertEqual(count_by_dept([]), {})

if __name__ == "__main__":
    unittest.main()
