import json
import tempfile
import unittest
from pathlib import Path

from task1_csv_to_json import count_by_dept, filter_by_admission, read_csv, write_json


class TestTask1(unittest.TestCase):
    def test_filter_keeps_correct_rows(self):
        rows = [
            {"入學方式": "聯合登記分發", "系所名稱": "資訊工程系"},
            {"入學方式": "甄選入學", "系所名稱": "電機工程系"},
        ]
        result = filter_by_admission(rows, "聯合登記分發")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["系所名稱"], "資訊工程系")

    def test_filter_removes_others(self):
        rows = [
            {"入學方式": "甄選入學"},
            {"入學方式": "聯合登記分發"},
            {"入學方式": "繁星推甄"},
        ]
        result = filter_by_admission(rows, "聯合登記分發")
        self.assertEqual(result, [{"入學方式": "聯合登記分發"}])

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

    def test_read_csv_reads_rows(self):
        csv_text = "學號,入學方式,系所名稱\nA001,聯合登記分發,資訊工程系\n"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.csv"
            path.write_text(csv_text, encoding="utf-8-sig")
            rows = read_csv(str(path))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["學號"], "A001")

    def test_write_json_writes_file(self):
        payload = {"ok": True, "count": 1}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "result.json"
            write_json(payload, str(path))
            loaded = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(loaded, payload)


if __name__ == "__main__":
    unittest.main()
