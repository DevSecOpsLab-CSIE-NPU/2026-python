import unittest
import sys
import os
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from task2_json_to_xml import build_xml_tree


class TestTask2(unittest.TestCase):

    def test_root_tag_and_attrs(self):
        data = {
            "來源": "113年新生資料庫",
            "總人數": 3,
            "學生清單": [],
        }
        root = build_xml_tree(data)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.get("total"), "3")

    def test_student_count_matches(self):
        data = {
            "來源": "113年新生資料庫",
            "總人數": 2,
            "學生清單": [
                {"學號": "001", "系所名稱": "A", "畢業學校": "B", "郵遞區號": "100"},
                {"學號": "002", "系所名稱": "C", "畢業學校": "D", "郵遞區號": "200"},
            ],
        }
        root = build_xml_tree(data)
        students = root.findall("student")
        self.assertEqual(len(students), 2)

    def test_student_attrs_exist(self):
        data = {
            "來源": "113年新生資料庫",
            "總人數": 1,
            "學生清單": [
                {"學號": "001", "系所名稱": "A", "畢業學校": "B", "郵遞區號": "100"},
            ],
        }
        root = build_xml_tree(data)
        student = root.find("student")
        self.assertIsNotNone(student)
        self.assertIsNotNone(student.get("id"))
        self.assertIsNotNone(student.get("dept"))
        self.assertIsNotNone(student.get("school"))
        self.assertIsNotNone(student.get("zip"))

    def test_empty_student_list(self):
        data = {
            "來源": "113年新生資料庫",
            "總人數": 0,
            "學生清單": [],
        }
        root = build_xml_tree(data)
        self.assertEqual(root.get("total"), "0")
        students = root.findall("student")
        self.assertEqual(len(students), 0)

    def test_xml_is_valid(self):
        data = {
            "來源": "113年新生資料庫",
            "總人數": 1,
            "學生清單": [
                {"學號": "001", "系所名稱": "A", "畢業學校": "B", "郵遞區號": "100"},
            ],
        }
        root = build_xml_tree(data)
        xml_str = ET.tostring(root, encoding="unicode")
        parsed = ET.fromstring(xml_str)
        self.assertEqual(parsed.tag, "students")


if __name__ == "__main__":
    unittest.main()
