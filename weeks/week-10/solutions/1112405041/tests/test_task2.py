import unittest
import os
import sys
import xml.etree.ElementTree as ET

# 將當前目錄加入 path 以便 import 解決
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from task2_json_to_xml import build_xml_tree
except ImportError:
    build_xml_tree = None

class TestTask2(unittest.TestCase):
    def test_root_tag_and_attrs(self):
        """測試根標籤與屬性是否正確"""
        if build_xml_tree is None:
            self.fail("build_xml_tree 尚未實作 (Red Stage)")

        data = {
            "來源": "測試來源",
            "總人數": 2,
            "學生清單": []
        }
        root = build_xml_tree(data)
        self.assertEqual(root.tag, "students")
        self.assertEqual(root.get("source"), "測試來源")
        self.assertEqual(root.get("total"), "2")

    def test_student_count_matches(self):
        """測試 XML 中學生節點數量是否正確"""
        if build_xml_tree is None:
            self.fail("build_xml_tree 尚未實作 (Red Stage)")

        data = {
            "來源": "測試",
            "總人數": 2,
            "學生清單": [
                {"學號": "S1", "系所名稱": "A", "畢業學校": "X", "郵遞區號": "1"},
                {"學號": "S2", "系所名稱": "B", "畢業學校": "Y", "郵遞區號": "2"}
            ]
        }
        root = build_xml_tree(data)
        self.assertEqual(len(root.findall("student")), 2)

    def test_student_attrs_exist(self):
        """測試每個學生節點的屬性是否完整"""
        if build_xml_tree is None:
            self.fail("build_xml_tree 尚未實作 (Red Stage)")

        data = {
            "來源": "測試",
            "總人數": 1,
            "學生清單": [
                {"學號": "S1", "系所名稱": "A系", "畢業學校": "某中", "郵遞區號": "880"}
            ]
        }
        root = build_xml_tree(data)
        student = root.find("student")
        self.assertEqual(student.get("id"), "S1")
        self.assertEqual(student.get("dept"), "A系")
        self.assertEqual(student.get("school"), "某中")
        self.assertEqual(student.get("zip"), "880")

    def test_empty_student_list(self):
        """測試學生清單為空的情況"""
        if build_xml_tree is None:
            self.fail("build_xml_tree 尚未實作 (Red Stage)")

        data = {
            "來源": "測試",
            "總人數": 0,
            "學生清單": []
        }
        root = build_xml_tree(data)
        self.assertEqual(root.get("total"), "0")
        self.assertEqual(len(root.findall("student")), 0)

    def test_xml_is_valid(self):
        """測試產生的 XML 結構是否有效"""
        if build_xml_tree is None:
            self.fail("build_xml_tree 尚未實作 (Red Stage)")

        data = {"來源": "T", "總人數": 0, "學生清單": []}
        root = build_xml_tree(data)
        xml_str = ET.tostring(root, encoding='utf-8')
        try:
            parsed_root = ET.fromstring(xml_str)
            self.assertEqual(parsed_root.tag, "students")
        except Exception:
            self.fail("產生的 XML 無法被解析")

if __name__ == "__main__":
    unittest.main()
