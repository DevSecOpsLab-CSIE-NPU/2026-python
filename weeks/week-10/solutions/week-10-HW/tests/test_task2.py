import unittest
import xml.etree.ElementTree as ET
from task2_json_to_xml import build_xml_tree

class TestTask2(unittest.TestCase):
    def test_root_tag_and_attrs(self):
        data = {
            "來源": "113年新生資料庫",
            "總人數": 42,
            "學生清單": []
        }
        root = build_xml_tree(data)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib["source"], "113年新生資料庫")
        self.assertEqual(root.attrib["total"], "42")
        
    def test_student_count_matches(self):
        data = {
            "來源": "113年新生資料庫",
            "總人數": 2,
            "學生清單": [
                {"學號": "1001", "系所名稱": "資工", "畢業學校": "高中A", "郵遞區號": "100"},
                {"學號": "1002", "系所名稱": "電機", "畢業學校": "高中B", "郵遞區號": "200"}
            ]
        }
        root = build_xml_tree(data)
        self.assertEqual(len(list(root)), 2)
        
    def test_student_attrs_exist(self):
        data = {
            "來源": "113年新生資料庫",
            "總人數": 1,
            "學生清單": [
                {"學號": "1001", "系所名稱": "資工", "畢業學校": "高中A", "郵遞區號": "100"}
            ]
        }
        root = build_xml_tree(data)
        student = root[0]
        self.assertEqual(student.attrib["id"], "1001")
        self.assertEqual(student.attrib["dept"], "資工")
        self.assertEqual(student.attrib["school"], "高中A")
        self.assertEqual(student.attrib["zip"], "100")
        
    def test_empty_student_list(self):
        data = {
            "來源": "測試",
            "總人數": 0,
            "學生清單": []
        }
        root = build_xml_tree(data)
        self.assertEqual(len(list(root)), 0)
        self.assertEqual(root.attrib["total"], "0")
        
    def test_xml_is_valid(self):
        data = {
            "來源": "測試",
            "總人數": 1,
            "學生清單": [
                {"學號": "1001", "系所名稱": "資工", "畢業學校": "高中A", "郵遞區號": "100"}
            ]
        }
        root = build_xml_tree(data)
        xml_str = ET.tostring(root, encoding="utf-8").decode("utf-8")
        parsed_root = ET.fromstring(xml_str)
        self.assertEqual(parsed_root.tag, "students")

if __name__ == '__main__':
    unittest.main()
