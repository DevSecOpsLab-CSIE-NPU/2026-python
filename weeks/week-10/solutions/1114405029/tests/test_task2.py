import unittest
import xml.etree.ElementTree as ET

from task2_json_to_xml import build_xml_tree


class TestTask2(unittest.TestCase):

    def test_root_tag_and_attrs(self):
        data = {
            "來源": "113年新生資料庫",
            "學生清單": [
                {"學號": "001"}
            ]
        }

        root = build_xml_tree(data)

        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib["total"], "1")

    def test_student_count_matches(self):
        data = {
            "學生清單": [
                {"學號": "001"},
                {"學號": "002"},
            ]
        }

        root = build_xml_tree(data)

        students = root.findall("student")

        self.assertEqual(len(students), 2)

    def test_student_attrs_exist(self):
        data = {
            "學生清單": [
                {
                    "學號": "001",
                    "系所名稱": "資訊工程系",
                    "畢業學校": "馬公高中",
                    "郵遞區號": "880",
                }
            ]
        }

        root = build_xml_tree(data)

        student = root.find("student")

        self.assertIn("id", student.attrib)
        self.assertIn("dept", student.attrib)
        self.assertIn("school", student.attrib)
        self.assertIn("zip", student.attrib)

    def test_empty_student_list(self):
        data = {
            "學生清單": []
        }

        root = build_xml_tree(data)

        self.assertEqual(root.attrib["total"], "0")

    def test_xml_is_valid(self):
        data = {
            "學生清單": [
                {
                    "學號": "001",
                    "系所名稱": "資訊工程系",
                    "畢業學校": "馬公高中",
                    "郵遞區號": "880",
                }
            ]
        }

        root = build_xml_tree(data)

        xml_string = ET.tostring(root, encoding="unicode")

        parsed = ET.fromstring(xml_string)

        self.assertEqual(parsed.tag, "students")


if __name__ == "__main__":
    unittest.main()