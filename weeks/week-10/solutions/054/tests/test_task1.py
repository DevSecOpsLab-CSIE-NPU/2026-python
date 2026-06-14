import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task1_csv_to_json import filter_by_admission, count_by_dept


class TestTask1(unittest.TestCase):

    def test_filter_keeps_correct_rows(self):
        rows = [
            {"入學方式": "聯合登記分發", "系所名稱": "資訊工程系"},
            {"入學方式": "繁星推甄", "系所名稱": "電機工程系"},
        ]
        result = filter_by_admission(rows, "聯合登記分發")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["系所名稱"], "資訊工程系")

    def test_filter_removes_others(self):
        rows = [
            {"入學方式": "繁星推甄", "系所名稱": "電機工程系"},
            {"入學方式": "申請入學", "系所名稱": "資訊工程系"},
        ]
        result = filter_by_admission(rows, "聯合登記分發")
        self.assertEqual(len(result), 0)

    def test_filter_empty_input(self):
        result = filter_by_admission([], "聯合登記分發")
        self.assertEqual(result, [])

    def test_count_by_dept_correct(self):
        rows = [
            {"系所名稱": "電機工程系"},
            {"系所名稱": "資訊工程系"},
            {"系所名稱": "電機工程系"},
        ]
        result = count_by_dept(rows)
        self.assertEqual(result, {"電機工程系": 2, "資訊工程系": 1})

    def test_count_by_dept_empty(self):
        result = count_by_dept([])
        self.assertEqual(result, {})

    def test_filter_partial_match(self):
        rows = [
            {"入學方式": "聯合登記分發", "系所名稱": "A"},
            {"入學方式": "聯合登記分發", "系所名稱": "B"},
            {"入學方式": "繁星推甄", "系所名稱": "C"},
        ]
        result = filter_by_admission(rows, "繁星推甄")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["系所名稱"], "C")


if __name__ == "__main__":
    unittest.main()
