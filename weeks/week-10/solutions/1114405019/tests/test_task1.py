import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task1_csv_to_json import filter_by_admission, count_by_dept


class TestFilterByAdmission(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {'入學方式': '聯合登記分發', '系所名稱': '資訊工程系', '學號': 'S001', '畢業學校': '高中A', '郵遞區號': '880'},
            {'入學方式': '甄選入學',    '系所名稱': '電機工程系', '學號': 'S002', '畢業學校': '高中B', '郵遞區號': '802'},
            {'入學方式': '聯合登記分發', '系所名稱': '電機工程系', '學號': 'S003', '畢業學校': '高中C', '郵遞區號': '330'},
            {'入學方式': '甄試分發入學', '系所名稱': '機械工程系', '學號': 'S004', '畢業學校': '高中D', '郵遞區號': '400'},
        ]

    def test_filter_keeps_correct_rows(self):
        result = filter_by_admission(self.rows, '聯合登記分發')
        self.assertEqual(len(result), 2)
        self.assertTrue(all(r['入學方式'] == '聯合登記分發' for r in result))

    def test_filter_removes_others(self):
        result = filter_by_admission(self.rows, '聯合登記分發')
        admission_types = {r['入學方式'] for r in result}
        self.assertNotIn('甄選入學', admission_types)
        self.assertNotIn('甄試分發入學', admission_types)

    def test_filter_empty_input(self):
        result = filter_by_admission([], '聯合登記分發')
        self.assertEqual(result, [])

    def test_filter_no_match_returns_empty(self):
        result = filter_by_admission(self.rows, '不存在的方式')
        self.assertEqual(result, [])


class TestCountByDept(unittest.TestCase):
    def test_count_by_dept_correct(self):
        rows = [
            {'系所名稱': '資訊工程系'},
            {'系所名稱': '電機工程系'},
            {'系所名稱': '資訊工程系'},
            {'系所名稱': '資訊工程系'},
        ]
        result = count_by_dept(rows)
        self.assertEqual(result['資訊工程系'], 3)
        self.assertEqual(result['電機工程系'], 1)

    def test_count_by_dept_empty(self):
        result = count_by_dept([])
        self.assertEqual(result, {})

    def test_count_by_dept_single(self):
        rows = [{'系所名稱': '應用外語系'}]
        result = count_by_dept(rows)
        self.assertEqual(result, {'應用外語系': 1})


if __name__ == '__main__':
    unittest.main()
