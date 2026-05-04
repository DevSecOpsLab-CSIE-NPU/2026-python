from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path
import unittest


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from task1_csv_to_json import build_summary, count_by_dept, filter_by_admission, read_csv, write_json


class TestTask1(unittest.TestCase):
    def setUp(self) -> None:
        self.rows = [
            {"學號": "1", "系所名稱": "資訊系", "入學方式": "聯合登記分發", "畢業學校": "A 高中", "郵遞區號": "100"},
            {"學號": "2", "系所名稱": "電機系", "入學方式": "繁星推甄", "畢業學校": "B 高中", "郵遞區號": "200"},
            {"學號": "3", "系所名稱": "資訊系", "入學方式": "聯合登記分發", "畢業學校": "C 高中", "郵遞區號": "300"},
        ]

    def test_filter_keeps_correct_rows(self):
        result = filter_by_admission(self.rows, "聯合登記分發")
        self.assertTrue(all(row["入學方式"] == "聯合登記分發" for row in result))
        self.assertEqual(len(result), 2)

    def test_filter_removes_others(self):
        result = filter_by_admission(self.rows, "聯合登記分發")
        self.assertNotIn({"學號": "2", "系所名稱": "電機系", "入學方式": "繁星推甄", "畢業學校": "B 高中", "郵遞區號": "200"}, result)

    def test_filter_empty_input(self):
        self.assertEqual(filter_by_admission([], "聯合登記分發"), [])

    def test_count_by_dept_correct(self):
        filtered = filter_by_admission(self.rows, "聯合登記分發")
        self.assertEqual(count_by_dept(filtered), {"資訊系": 2})

    def test_count_by_dept_empty(self):
        self.assertEqual(count_by_dept([]), {})

    def test_build_summary_structure(self):
        summary = build_summary(self.rows)
        self.assertEqual(summary["來源"], "113年新生資料庫")
        self.assertEqual(summary["入學方式篩選"], "聯合登記分發")
        self.assertEqual(summary["總人數"], 2)
        self.assertEqual(len(summary["學生清單"]), 2)

    def test_read_and_write_json_round_trip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "sample.csv"
            json_path = Path(temp_dir) / "out.json"
            csv_path.write_text(
                "學號,系所名稱,入學方式,畢業學校,郵遞區號\n"
                "1,資訊系,聯合登記分發,A 高中,100\n",
                encoding="utf-8",
            )
            rows = read_csv(str(csv_path))
            self.assertEqual(len(rows), 1)

            write_json(build_summary(rows), str(json_path))
            written = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(written["總人數"], 1)


if __name__ == "__main__":
    unittest.main()