"""Task 2 的單元測試。"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET


TEST_DIR = Path(__file__).resolve().parent
SOLUTIONS_DIR = TEST_DIR.parent
if str(SOLUTIONS_DIR) not in sys.path:
    sys.path.insert(0, str(SOLUTIONS_DIR))

from task2_json_to_xml import build_xml_tree
from task2_json_to_xml import read_json
from task2_json_to_xml import write_xml


class TestTask2(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            "來源": "113年新生資料庫",
            "總人數": 2,
            "學生清單": [
                {"學號": "1131234001", "系所名稱": "資訊系", "畢業學校": "測試高中A", "郵遞區號": "100"},
                {"學號": "1131234002", "系所名稱": "電機系", "畢業學校": "測試高中B", "郵遞區號": "200"},
            ],
        }

    def test_root_tag_and_attrs(self):
        root = build_xml_tree(self.sample_data)

        self.assertEqual(root.tag, "students")
        self.assertEqual(root.get("total"), "2")
        self.assertEqual(root.get("source"), "113年新生資料庫")

    def test_student_count_matches(self):
        root = build_xml_tree(self.sample_data)

        self.assertEqual(len(root.findall("student")), len(self.sample_data["學生清單"]))

    def test_student_attrs_exist(self):
        root = build_xml_tree(self.sample_data)

        for student in root.findall("student"):
            self.assertIn("id", student.attrib)
            self.assertIn("dept", student.attrib)
            self.assertIn("school", student.attrib)
            self.assertIn("zip", student.attrib)

    def test_empty_student_list(self):
        root = build_xml_tree({"來源": "113年新生資料庫", "學生清單": []})

        self.assertEqual(root.get("total"), "0")
        self.assertEqual(root.findall("student"), [])

    def test_xml_is_valid(self):
        root = build_xml_tree(self.sample_data)
        xml_text = ET.tostring(root, encoding="unicode")

        parsed = ET.fromstring(xml_text)
        self.assertEqual(parsed.tag, "students")

    def test_read_json_and_write_xml_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_dir_path = Path(tmp_dir)
            json_path = tmp_dir_path / "sample.json"
            xml_path = tmp_dir_path / "sample.xml"

            with open(json_path, "w", encoding="utf-8") as file_handle:
                json.dump(self.sample_data, file_handle, ensure_ascii=False)

            data = read_json(str(json_path))
            self.assertEqual(data["來源"], "113年新生資料庫")

            write_xml(data, str(xml_path))
            self.assertTrue(xml_path.exists())

            tree = ET.parse(xml_path)
            self.assertEqual(tree.getroot().get("total"), "2")


if __name__ == "__main__":
    unittest.main()