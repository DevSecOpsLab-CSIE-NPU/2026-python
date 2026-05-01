import unittest

from task1_csv_to_json import (
    filter_by_admission,
    count_by_dept,
)


class TestTask1(unittest.TestCase):

    def test_filter_keeps_correct_rows(self):
        rows = [
            {"入學方式": "聯合登記分發", "系所名稱": "資訊工程系"},
            {"入學方式": "繁星推薦", "系所名稱": "電機工程系"},
        ]

        result = filter_by_admission(rows, "聯合登記分發")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["系所名稱"], "資訊工程系")

    def test_filter_removes_others(self):
        rows = [
            {"入學方式": "繁星推薦"},
            {"入學方式": "個人申請"},
        ]

        result = filter_by_admission(rows, "聯合登記分發")

        self.assertEqual(result, [])

    def test_filter_empty_input(self):
        result = filter_by_admission([], "聯合登記分發")
        self.assertEqual(result, [])

    def test_count_by_dept_correct(self):
        rows = [
            {"系所名稱": "資訊工程系"},
            {"系所名稱": "資訊工程系"},
            {"系所名稱": "電機工程系"},
        ]

        result = count_by_dept(rows)

        self.assertEqual(result["資訊工程系"], 2)
        self.assertEqual(result["電機工程系"], 1)

    def test_count_by_dept_empty(self):
        result = count_by_dept([])
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()