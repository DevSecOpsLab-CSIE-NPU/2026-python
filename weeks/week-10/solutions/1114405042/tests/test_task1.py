"""Task 1 的單元測試。"""

from __future__ import annotations

import csv
import json
import sys
import tempfile
from pathlib import Path
import unittest


TEST_DIR = Path(__file__).resolve().parent
SOLUTIONS_DIR = TEST_DIR.parent
if str(SOLUTIONS_DIR) not in sys.path:
    sys.path.insert(0, str(SOLUTIONS_DIR))

from task1_csv_to_json import count_by_dept
from task1_csv_to_json import filter_by_admission
from task1_csv_to_json import read_csv
from task1_csv_to_json import write_json


class TestTask1(unittest.TestCase):
    def test_filter_keeps_correct_rows(self):
        rows = [
            {"入學方式": "聯合登記分發", "系所名稱": "資訊系"},
            {"入學方式": "繁星推甄", "系所名稱": "電機系"},
        ]

        result = filter_by_admission(rows, "聯合登記分發")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["系所名稱"], "資訊系")

    def test_filter_removes_others(self):
        rows = [
            {"入學方式": "聯合登記分發", "系所名稱": "資訊系"},
            {"入學方式": "申請入學", "系所名稱": "機械系"},
            {"入學方式": "繁星推甄", "系所名稱": "電機系"},
        ]

        result = filter_by_admission(rows, "聯合登記分發")

        self.assertTrue(all(row["入學方式"] == "聯合登記分發" for row in result))
        self.assertEqual({row["系所名稱"] for row in result}, {"資訊系"})

    def test_filter_empty_input(self):
        self.assertEqual(filter_by_admission([], "聯合登記分發"), [])

    def test_count_by_dept_correct(self):
        rows = [
            {"系所名稱": "資訊系"},
            {"系所名稱": "資訊系"},
            {"系所名稱": "電機系"},
        ]

        self.assertEqual(count_by_dept(rows), {"資訊系": 2, "電機系": 1})

    def test_count_by_dept_empty(self):
        self.assertEqual(count_by_dept([]), {})

    def test_read_csv_and_write_json_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_dir_path = Path(tmp_dir)
            csv_path = tmp_dir_path / "sample.csv"
            json_path = tmp_dir_path / "sample.json"

            with open(csv_path, "w", encoding="utf-8", newline="") as file_handle:
                writer = csv.DictWriter(file_handle, fieldnames=["學號", "入學方式", "系所名稱", "畢業學校", "郵遞區號"])
                writer.writeheader()
                writer.writerow(
                    {
                        "學號": "1131234001",
                        "入學方式": "聯合登記分發",
                        "系所名稱": "資訊系",
                        "畢業學校": "測試高中",
                        "郵遞區號": "100",
                    }
                )

            rows = read_csv(str(csv_path))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["學號"], "1131234001")

            write_json({"rows": rows}, str(json_path))
            with open(json_path, encoding="utf-8") as file_handle:
                payload = json.load(file_handle)
            self.assertEqual(payload["rows"][0]["系所名稱"], "資訊系")


if __name__ == "__main__":
    unittest.main()