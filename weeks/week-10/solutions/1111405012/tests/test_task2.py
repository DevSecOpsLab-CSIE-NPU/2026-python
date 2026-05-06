import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from task2_json_to_xml import build_xml_tree, write_xml  # noqa: E402


class TestTask2JsonToXml(unittest.TestCase):
    def setUp(self):
        self.data = {
            "來源": "113年新生資料庫",
            "總人數": 2,
            "學生清單": [
                {
                    "學號": "1130001",
                    "系所名稱": "資訊工程系",
                    "畢業學校": "澎湖高中",
                    "郵遞區號": "880",
                },
                {
                    "學號": "1130002",
                    "系所名稱": "電機工程系",
                    "畢業學校": "馬公高中",
                    "郵遞區號": "880",
                },
            ],
        }

    def test_root_tag_and_attrs(self):
        root = build_xml_tree(self.data)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.get("source"), "113年新生資料庫")
        self.assertEqual(root.get("total"), "2")

    def test_student_count_matches(self):
        root = build_xml_tree(self.data)
        self.assertEqual(len(root.findall("student")), 2)

    def test_student_attrs_exist(self):
        root = build_xml_tree(self.data)
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
        root = build_xml_tree(self.data)
        xml_text = ET.tostring(root, encoding="unicode")
        parsed = ET.fromstring(xml_text)
        self.assertEqual(parsed.tag, "students")

    def test_write_xml_creates_parseable_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "students.xml"
            write_xml(self.data, output_path)
            root = ET.parse(output_path).getroot()
        self.assertEqual(root.get("total"), "2")


if __name__ == "__main__":
    unittest.main()
