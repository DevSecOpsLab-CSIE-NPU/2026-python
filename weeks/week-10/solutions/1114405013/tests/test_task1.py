import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from task1_csv_to_json import build_output_data, count_by_dept, filter_by_admission

class TestTask1(unittest.TestCase):
    def test_filter_keeps_correct_rows(self):
        rows = [{"入學方式": "聯合登記分發", "系所名稱": "資訊工程系"}, {"入學方式": "繁星推甄", "系所名稱": "電機工程系"}]
        result = filter_by_admission(rows, "聯合登記分發")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["系所名稱"], "資訊工程系")
    def test_filter_removes_others(self):
        rows = [{"入學方式": "聯合登記分發"}, {"入學方式": "個人申請"}, {"入學方式": "分科測驗"}]
        self.assertTrue(all(r["入學方式"] == "聯合登記分發" for r in filter_by_admission(rows, "聯合登記分發")))
    def test_filter_empty_input(self):
        self.assertEqual(filter_by_admission([], "聯合登記分發"), [])
    def test_count_by_dept_correct(self):
        rows = [{"系所名稱": "資訊工程系"}, {"系所名稱": "資訊工程系"}, {"系所名稱": "電機工程系"}]
        self.assertEqual(count_by_dept(rows), {"資訊工程系": 2, "電機工程系": 1})
    def test_count_by_dept_empty(self):
        self.assertEqual(count_by_dept([]), {})
    def test_count_by_dept_ignores_missing_or_blank(self):
        self.assertEqual(count_by_dept([{"系所名稱": "資訊工程系"}, {"系所名稱": ""}, {}]), {"資訊工程系": 1})
    def test_build_output_data_total_matches_students(self):
        rows = [{"學號": "1130001", "系所名稱": "資訊工程系", "入學方式": "聯合登記分發", "畢業學校": "國立馬公高中", "郵遞區號": "880"}]
        data = build_output_data(rows)
        self.assertEqual(data["總人數"], len(data["學生清單"]))

if __name__ == "__main__":
    unittest.main()
