import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from task2_json_to_xml import build_xml_tree, read_json, write_xml


class TestTask2(unittest.TestCase):
    def setUp(self):
        self.sample = {
            "來源": "113年新生資料庫",
            "學生清單": [
                {"學號": "S001", "系所名稱": "資訊工程系", "畢業學校": "馬公高中", "郵遞區號": "880"},
                {"學號": "S002", "系所名稱": "電機工程系", "畢業學校": "中山高中", "郵遞區號": "700"},
            ],
        }

    def test_root_tag_and_attrs(self):
        root = build_xml_tree(self.sample)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.get("total"), "2")

    def test_student_count_matches(self):
        root = build_xml_tree(self.sample)
        self.assertEqual(len(root.findall("student")), len(self.sample["學生清單"]))

    def test_student_attrs_exist(self):
        root = build_xml_tree(self.sample)
        student = root.find("student")
        self.assertIsNotNone(student)
        for key in ["id", "dept", "school", "zip"]:
            self.assertIn(key, student.attrib)

    def test_empty_student_list(self):
        root = build_xml_tree({"來源": "113年新生資料庫", "學生清單": []})
        self.assertEqual(root.get("total"), "0")
        self.assertEqual(len(root.findall("student")), 0)

    def test_xml_is_valid(self):
        root = build_xml_tree(self.sample)
        xml_str = ET.tostring(root, encoding="utf-8")
        parsed = ET.fromstring(xml_str)
        self.assertEqual(parsed.tag, "students")

    def test_read_json_reads_dict(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "data.json"
            path.write_text('{"來源":"x","學生清單":[]}', encoding="utf-8")
            data = read_json(str(path))
        self.assertEqual(data["來源"], "x")

    def test_write_xml_outputs_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "students.xml"
            write_xml(self.sample, str(path))
            content = path.read_text(encoding="utf-8")
        self.assertIn("<students", content)
        self.assertIn("<student", content)


if __name__ == "__main__":
    unittest.main()
