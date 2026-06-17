from __future__ import annotations

import sys
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

PROJECT_DIR = Path(__file__).resolve().parents[1]
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from task2_json_to_xml import build_xml_tree

SAMPLE = {
    "來源": "113年新生資料庫",
    "學生清單": [
        {
            "學號": "S001",
            "系所名稱": "資訊工程系",
            "畢業學校": "國立馬公高中",
            "郵遞區號": "880",
        },
        {
            "學號": "S002",
            "系所名稱": "電機工程系",
            "畢業學校": "國立澎湖海事",
            "郵遞區號": "880",
        },
    ],
}


class TestTask2(unittest.TestCase):
    def test_root_tag_and_attrs(self):
        root = build_xml_tree(SAMPLE)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib.get("total"), "2")

    def test_student_count_matches(self):
        root = build_xml_tree(SAMPLE)
        self.assertEqual(len(root.findall("student")), len(SAMPLE["學生清單"]))

    def test_student_attrs_exist(self):
        root = build_xml_tree(SAMPLE)
        student = root.find("student")
        self.assertIsNotNone(student)
        for key in ["id", "dept", "school", "zip"]:
            self.assertIn(key, student.attrib)

    def test_empty_student_list(self):
        root = build_xml_tree({"來源": "113年新生資料庫", "學生清單": []})
        self.assertEqual(root.attrib.get("total"), "0")

    def test_xml_is_valid(self):
        root = build_xml_tree(SAMPLE)
        xml_text = ET.tostring(root, encoding="utf-8")
        parsed = ET.fromstring(xml_text)
        self.assertEqual(parsed.tag, "students")


if __name__ == "__main__":
    unittest.main()
