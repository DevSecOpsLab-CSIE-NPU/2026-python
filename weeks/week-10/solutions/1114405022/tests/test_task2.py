from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path
import unittest
from xml.etree import ElementTree as ET


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from task2_json_to_xml import build_xml_tree, read_json, write_xml


class TestTask2(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {
            "來源": "113年新生資料庫",
            "入學方式篩選": "聯合登記分發",
            "總人數": 2,
            "系所統計": {"資訊系": 2},
            "學生清單": [
                {"學號": "1", "系所名稱": "資訊系", "畢業學校": "A 高中", "郵遞區號": "100"},
                {"學號": "3", "系所名稱": "資訊系", "畢業學校": "C 高中", "郵遞區號": "300"},
            ],
        }

    def test_root_tag_and_attrs(self):
        root = build_xml_tree(self.data)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib["source"], "113年新生資料庫")
        self.assertEqual(root.attrib["total"], "2")

    def test_student_count_matches(self):
        root = build_xml_tree(self.data)
        self.assertEqual(len(root.findall("student")), 2)

    def test_student_attrs_exist(self):
        root = build_xml_tree(self.data)
        first_student = root.find("student")
        self.assertIsNotNone(first_student)
        self.assertEqual(first_student.attrib["id"], "1")
        self.assertEqual(first_student.attrib["dept"], "資訊系")
        self.assertEqual(first_student.attrib["school"], "A 高中")
        self.assertEqual(first_student.attrib["zip"], "100")

    def test_empty_student_list(self):
        root = build_xml_tree({"來源": "113年新生資料庫", "學生清單": []})
        self.assertEqual(root.attrib["total"], "0")
        self.assertEqual(len(root.findall("student")), 0)

    def test_xml_is_valid(self):
        root = build_xml_tree(self.data)
        xml_text = ET.tostring(root, encoding="unicode")
        parsed = ET.fromstring(xml_text)
        self.assertEqual(parsed.tag, "students")

    def test_read_and_write_json_xml_round_trip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            json_path = Path(temp_dir) / "sample.json"
            xml_path = Path(temp_dir) / "sample.xml"
            json_path.write_text(json.dumps(self.data, ensure_ascii=False), encoding="utf-8")

            loaded = read_json(str(json_path))
            self.assertEqual(loaded["總人數"], 2)

            write_xml(loaded, str(xml_path))
            parsed = ET.parse(xml_path)
            self.assertEqual(parsed.getroot().attrib["total"], "2")


if __name__ == "__main__":
    unittest.main()