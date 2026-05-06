import json
import sys
import tempfile
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from task1_csv_to_json import (  # noqa: E402
    build_output,
    count_by_dept,
    filter_by_admission,
    write_json,
)


class TestTask1CsvToJson(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {
                "學號": "1130001",
                "系所名稱": "資訊工程系",
                "入學方式": "聯合登記分發",
                "畢業學校": "澎湖高中",
                "郵遞區號": "880",
            },
            {
                "學號": "1130002",
                "系所名稱": "電機工程系",
                "入學方式": "甄選入學",
                "畢業學校": "馬公高中",
                "郵遞區號": "880",
            },
            {
                "學號": "1130003",
                "系所名稱": "資訊工程系",
                "入學方式": "聯合登記分發",
                "畢業學校": "台南一中",
                "郵遞區號": "700",
            },
        ]

    def test_filter_keeps_correct_rows(self):
        result = filter_by_admission(self.rows, "聯合登記分發")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(row["入學方式"] == "聯合登記分發" for row in result))

    def test_filter_removes_others(self):
        result = filter_by_admission(self.rows, "聯合登記分發")
        ids = {row["學號"] for row in result}
        self.assertNotIn("1130002", ids)

    def test_filter_empty_input(self):
        self.assertEqual(filter_by_admission([], "聯合登記分發"), [])

    def test_count_by_dept_correct(self):
        filtered = filter_by_admission(self.rows, "聯合登記分發")
        self.assertEqual(count_by_dept(filtered), {"資訊工程系": 2})

    def test_count_by_dept_empty(self):
        self.assertEqual(count_by_dept([]), {})

    def test_build_output_contains_required_fields(self):
        result = build_output(self.rows, "聯合登記分發")
        self.assertEqual(result["總人數"], 2)
        self.assertEqual(result["系所統計"], {"資訊工程系": 2})
        self.assertEqual(
            set(result["學生清單"][0]),
            {"學號", "系所名稱", "畢業學校", "郵遞區號"},
        )

    def test_write_json_creates_utf8_json(self):
        data = build_output(self.rows, "聯合登記分發")
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "students.json"
            write_json(data, output_path)
            loaded = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual(loaded["入學方式篩選"], "聯合登記分發")


if __name__ == "__main__":
    unittest.main()
