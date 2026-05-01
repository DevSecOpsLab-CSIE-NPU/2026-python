import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from task1_csv_to_json import filter_by_admission, count_by_dept


class TestTask1(unittest.TestCase):

    def test_filter_keeps_correct_rows(self):
        rows = [
            {"入學方式": "聯合登記分發", "系所名稱": "電機工程系"},
            {"入學方式": "繁星推甄", "系所名稱": "資訊工程系"},
            {"入學方式": "聯合登記分發", "系所名稱": "機械工程系"},
        ]
        result = filter_by_admission(rows, "聯合登記分發")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(r["入學方式"] == "聯合登記分發" for r in result))

    def test_filter_removes_others(self):
        rows = [
            {"入學方式": "繁星推甄", "系所名稱": "電機系"},
            {"入學方式": "個人申請", "系所名稱": "資工系"},
            {"入學方式": "分科測驗", "系所名稱": "機械系"},
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
            {"系所名稱": "機械工程系"},
        ]
        result = count_by_dept(rows)
        expected = {"電機工程系": 2, "資訊工程系": 1, "機械工程系": 1}
        self.assertEqual(result, expected)

    def test_count_by_dept_empty(self):
        result = count_by_dept([])
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
