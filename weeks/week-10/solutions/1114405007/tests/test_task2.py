import sys
import os
import unittest
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from task2_json_to_xml import build_xml_tree


def _make_data(students=None, total=None):
    if students is None:
        students = [
            {"學號": "1131001", "系所名稱": "電機工程系", "畢業學校": "高中A", "郵遞區號": "880"},
            {"學號": "1131002", "系所名稱": "資訊工程系", "畢業學校": "高中B", "郵遞區號": "700"},
        ]
    if total is None:
        total = len(students)
    return {"來源": "113年新生資料庫", "總人數": total, "學生清單": students}


class TestBuildXmlTree(unittest.TestCase):

    # 正常：根標籤為 students，total 屬性正確
    def test_root_tag_and_attrs(self):
        root = build_xml_tree(_make_data())
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.attrib["total"], "2")
        self.assertEqual(root.attrib["source"], "113年新生資料庫")

    # 正常：XML 中 <student> 數量與學生清單一致
    def test_student_count_matches(self):
        root = build_xml_tree(_make_data())
        self.assertEqual(len(root.findall("student")), 2)

    # 正常：每個 <student> 包含 id, dept, school, zip 屬性
    def test_student_attrs_exist(self):
        root = build_xml_tree(_make_data())
        for child in root.findall("student"):
            self.assertIn("id", child.attrib)
            self.assertIn("dept", child.attrib)
            self.assertIn("school", child.attrib)
            self.assertIn("zip", child.attrib)

    # 邊界：學生清單為空時，total 屬性為 "0"
    def test_empty_student_list(self):
        root = build_xml_tree(_make_data(students=[], total=0))
        self.assertEqual(root.attrib["total"], "0")
        self.assertEqual(len(root.findall("student")), 0)

    # 反例：輸出的 XML 字串可被 ET.fromstring() 正常解析
    def test_xml_is_valid(self):
        root = build_xml_tree(_make_data())
        xml_str = ET.tostring(root, encoding="unicode")
        try:
            parsed = ET.fromstring(xml_str)
            self.assertEqual(parsed.tag, "students")
        except ET.ParseError as e:
            self.fail(f"XML 解析失敗: {e}")

    # 正常：學生屬性值正確對應
    def test_student_attr_values(self):
        root = build_xml_tree(_make_data())
        first = root.findall("student")[0]
        self.assertEqual(first.attrib["id"], "1131001")
        self.assertEqual(first.attrib["dept"], "電機工程系")
        self.assertEqual(first.attrib["zip"], "880")

    # 邊界：單一學生
    def test_single_student(self):
        data = _make_data(students=[
            {"學號": "1131999", "系所名稱": "機械工程系", "畢業學校": "高中Z", "郵遞區號": "100"}
        ], total=1)
        root = build_xml_tree(data)
        self.assertEqual(len(root.findall("student")), 1)
        self.assertEqual(root.attrib["total"], "1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
