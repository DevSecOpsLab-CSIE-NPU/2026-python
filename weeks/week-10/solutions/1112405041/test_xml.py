import unittest
import tempfile
import os
import xml.etree.ElementTree as ET
from task2_json_to_xml import build_xml_tree, write_xml

class TestXML(unittest.TestCase):

    def test_root_tag_and_attrs(self):
        data = {"來源": "test", "總人數": 2, "學生清單": []}
        root = build_xml_tree(data)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib.get("source"), "test")
        self.assertEqual(root.attrib.get("total"), "2")

    def test_student_count_matches(self):
        data = {
            "來源": "test", "總人數": 2,
            "學生清單": [
                {"學號": "A1", "系所名稱": "X", "畢業學校": "Y", "郵遞區號": "Z"},
                {"學號": "A2", "系所名稱": "X", "畢業學校": "Y", "郵遞區號": "Z"},
            ]
        }
        root = build_xml_tree(data)
        students = root.findall("student")
        self.assertEqual(len(students), 2)

    def test_student_attrs_exist(self):
        data = {
            "來源": "test", "總人數": 1,
            "學生清單": [
                {"學號": "A1", "系所名稱": "電機系", "畢業學校": "某高中", "郵遞區號": "880"},
            ]
        }
        root = build_xml_tree(data)
        s = root.find("student")
        self.assertEqual(s.attrib.get("id"), "A1")
        self.assertEqual(s.attrib.get("dept"), "電機系")
        self.assertEqual(s.attrib.get("school"), "某高中")
        self.assertEqual(s.attrib.get("zip"), "880")

    def test_empty_student_list(self):
        data = {"來源": "test", "總人數": 0, "學生清單": []}
        root = build_xml_tree(data)
        self.assertEqual(root.attrib.get("total"), "0")
        self.assertEqual(len(root.findall("student")), 0)

    def test_xml_is_valid(self):
        data = {"來源": "test", "總人數": 1, "學生清單": [{"學號": "A1", "系所名稱": "X", "畢業學校": "Y", "郵遞區號": "Z"}]}
        root = build_xml_tree(data)
        xml_str = ET.tostring(root, encoding="unicode")
        parsed = ET.fromstring(xml_str)
        self.assertEqual(parsed.tag, "students")

    def test_write_xml_output(self):
        data = {"來源": "test", "總人數": 1, "學生清單": [{"學號": "A1", "系所名稱": "X", "畢業學校": "Y", "郵遞區號": "Z"}]}
        tmp = tempfile.mktemp(suffix=".xml")
        write_xml(data, tmp)
        self.assertTrue(os.path.exists(tmp))
        tree = ET.parse(tmp)
        self.assertEqual(tree.getroot().tag, "students")
        os.unlink(tmp)
