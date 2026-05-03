from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from task1_csv_to_json import count_by_dept, filter_by_admission


class TestTask1(unittest.TestCase):
    def test_filter_keeps_correct_rows(self):
        rows = [
            {"入學方式": "聯合登記分發", "系所名稱": "資訊工程系"},
            {"入學方式": "個人申請", "系所名稱": "電機工程系"},
        ]
        result = filter_by_admission(rows, "聯合登記分發")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["系所名稱"], "資訊工程系")

    def test_filter_removes_others(self):
        rows = [
            {"入學方式": "繁星推甄", "系所名稱": "A"},
            {"入學方式": "聯合登記分發", "系所名稱": "B"},
            {"入學方式": "分科測驗", "系所名稱": "C"},
        ]
        result = filter_by_admission(rows, "聯合登記分發")
        self.assertEqual(result, [{"入學方式": "聯合登記分發", "系所名稱": "B"}])

    def test_filter_empty_input(self):
        self.assertEqual(filter_by_admission([], "聯合登記分發"), [])

    def test_count_by_dept_correct(self):
        rows = [
            {"系所名稱": "資訊工程系"},
            {"系所名稱": "資訊工程系"},
            {"系所名稱": "電機工程系"},
        ]
        self.assertEqual(count_by_dept(rows), {"資訊工程系": 2, "電機工程系": 1})

    def test_count_by_dept_empty(self):
        self.assertEqual(count_by_dept([]), {})


if __name__ == "__main__":
    unittest.main()
