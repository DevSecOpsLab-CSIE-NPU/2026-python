import sys, unittest, xml.etree.ElementTree as ET
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from task2_json_to_xml import build_xml_tree

class TestTask2(unittest.TestCase):
    def setUp(self):
        self.data = {"來源": "113年新生資料庫", "學生清單": [
            {"學號": "1130001", "系所名稱": "資訊工程系", "畢業學校": "國立馬公高中", "郵遞區號": "880"},
            {"學號": "1130002", "系所名稱": "電機工程系", "畢業學校": "國立澎湖高中", "郵遞區號": "885"},
        ]}
    def test_root_tag_and_attrs(self):
        root = build_xml_tree(self.data)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib["total"], "2")
    def test_student_count_matches(self):
        self.assertEqual(len(build_xml_tree(self.data).findall("student")), len(self.data["學生清單"]))
    def test_student_attrs_exist(self):
        for s in build_xml_tree(self.data).findall("student"):
            self.assertIn("id", s.attrib); self.assertIn("dept", s.attrib); self.assertIn("school", s.attrib); self.assertIn("zip", s.attrib)
    def test_empty_student_list(self):
        root = build_xml_tree({"來源": "113年新生資料庫", "學生清單": []})
        self.assertEqual(root.attrib["total"], "0")
        self.assertEqual(root.findall("student"), [])
    def test_xml_is_valid(self):
        parsed = ET.fromstring(ET.tostring(build_xml_tree(self.data), encoding="unicode"))
        self.assertEqual(parsed.tag, "students")
    def test_invalid_student_list_type(self):
        with self.assertRaises(ValueError):
            build_xml_tree({"來源": "113年新生資料庫", "學生清單": "wrong"})

if __name__ == "__main__":
    unittest.main()
