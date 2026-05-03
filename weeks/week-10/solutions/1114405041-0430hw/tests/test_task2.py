from __future__ import annotations

import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from task2_json_to_xml import build_xml_tree


class TestTask2(unittest.TestCase):
    def setUp(self):
        self.data = {
            "來源": "113年新生資料庫",
            "學生清單": [
                {
                    "學號": "1131234001",
                    "系所名稱": "電機工程系",
                    "畢業學校": "國立馬公高中",
                    "郵遞區號": "880",
                },
                {
                    "學號": "1131234002",
                    "系所名稱": "資訊工程系",
                    "畢業學校": "國立馬公高中",
                    "郵遞區號": "880",
                },
            ],
        }

    def test_root_tag_and_attrs(self):
        root = build_xml_tree(self.data)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib["total"], "2")

    def test_student_count_matches(self):
        root = build_xml_tree(self.data)
        students = root.findall("student")
        self.assertEqual(len(students), len(self.data["學生清單"]))

    def test_student_attrs_exist(self):
        root = build_xml_tree(self.data)
        first = root.find("student")
        self.assertIsNotNone(first)
        for attr in ["id", "dept", "school", "zip"]:
            self.assertIn(attr, first.attrib)

    def test_empty_student_list(self):
        root = build_xml_tree({"來源": "113年新生資料庫", "學生清單": []})
        self.assertEqual(root.attrib["total"], "0")
        self.assertEqual(root.findall("student"), [])

    def test_xml_is_valid(self):
        root = build_xml_tree(self.data)
        xml_str = ET.tostring(root, encoding="utf-8")
        parsed = ET.fromstring(xml_str)
        self.assertEqual(parsed.tag, "students")


if __name__ == "__main__":
    unittest.main()
