import unittest
import xml.etree.ElementTree as ET
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task2_json_to_xml import build_xml_tree


class TestTask2(unittest.TestCase):

    def test_root_tag_and_attrs(self):
        data = {"來源": "113年新生資料庫", "總人數": 2, "學生清單": []}
        root = build_xml_tree(data)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.get("source"), "113年新生資料庫")
        self.assertEqual(root.get("total"), "2")

    def test_student_count_matches(self):
        data = {
            "總人數": 2,
            "學生清單": [
                {"學號": "A1", "系所名稱": "電機系", "畢業學校": "S1", "郵遞區號": "100"},
                {"學號": "A2", "系所名稱": "資工系", "畢業學校": "S2", "郵遞區號": "200"},
            ],
        }
        root = build_xml_tree(data)
        students = root.findall("student")
        self.assertEqual(len(students), 2)

    def test_student_attrs_exist(self):
        data = {
            "總人數": 1,
            "學生清單": [
                {"學號": "A1", "系所名稱": "電機系", "畢業學校": "S1", "郵遞區號": "100"},
            ],
        }
        root = build_xml_tree(data)
        student = root.find("student")
        self.assertEqual(student.get("id"), "A1")
        self.assertEqual(student.get("dept"), "電機系")
        self.assertEqual(student.get("school"), "S1")
        self.assertEqual(student.get("zip"), "100")

    def test_empty_student_list(self):
        data = {"總人數": 0, "學生清單": []}
        root = build_xml_tree(data)
        self.assertEqual(root.get("total"), "0")
        self.assertEqual(len(root.findall("student")), 0)

    def test_xml_is_valid(self):
        data = {
            "總人數": 1,
            "學生清單": [
                {"學號": "A1", "系所名稱": "電機系", "畢業學校": "S1", "郵遞區號": "100"},
            ],
        }
        root = build_xml_tree(data)
        xml_str = ET.tostring(root, encoding="unicode")
        parsed = ET.fromstring(xml_str)
        self.assertEqual(parsed.tag, "students")

    def test_root_total_zero(self):
        data = {"來源": "test", "總人數": 0, "學生清單": []}
        root = build_xml_tree(data)
        self.assertEqual(root.get("total"), "0")


if __name__ == "__main__":
    unittest.main()
