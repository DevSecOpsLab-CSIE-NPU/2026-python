import unittest
import xml.etree.ElementTree as ET

from task2_json_to_xml import build_xml_tree


class TestTask2(unittest.TestCase):
    def setUp(self):
        self.sample = {
            "來源": "113年新生資料庫",
            "總人數": 2,
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
        root = build_xml_tree(self.sample)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib.get("source"), "113年新生資料庫")
        self.assertEqual(root.attrib.get("total"), "2")

    def test_student_count_matches(self):
        root = build_xml_tree(self.sample)
        self.assertEqual(len(root.findall("student")), 2)

    def test_student_attrs_exist(self):
        root = build_xml_tree(self.sample)
        for student in root.findall("student"):
            self.assertIn("id", student.attrib)
            self.assertIn("dept", student.attrib)
            self.assertIn("school", student.attrib)
            self.assertIn("zip", student.attrib)

    def test_empty_student_list(self):
        root = build_xml_tree({"來源": "113年新生資料庫", "學生清單": []})
        self.assertEqual(root.attrib.get("total"), "0")
        self.assertEqual(len(root.findall("student")), 0)

    def test_xml_is_valid(self):
        root = build_xml_tree(self.sample)
        xml_text = ET.tostring(root, encoding="utf-8").decode("utf-8")
        parsed = ET.fromstring(xml_text)
        self.assertEqual(parsed.tag, "students")


if __name__ == "__main__":
    unittest.main()
