import unittest
import sys
import os
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task2_json_to_xml import build_xml_tree


class TestBuildXmlTree(unittest.TestCase):
    def setUp(self):
        self.data = {
            '來源': '113年新生資料庫',
            '入學方式篩選': '聯合登記分發',
            '總人數': 2,
            '系所統計': {'資訊工程系': 1, '電機工程系': 1},
            '學生清單': [
                {'學號': 'S001', '系所名稱': '資訊工程系', '畢業學校': '國立馬公高中', '郵遞區號': '880'},
                {'學號': 'S002', '系所名稱': '電機工程系', '畢業學校': '私立立志高中', '郵遞區號': '802'},
            ],
        }

    def test_root_tag_and_attrs(self):
        root = build_xml_tree(self.data)
        self.assertEqual(root.tag, 'students')
        self.assertEqual(root.attrib['total'], '2')
        self.assertEqual(root.attrib['source'], '113年新生資料庫')

    def test_student_count_matches(self):
        root = build_xml_tree(self.data)
        self.assertEqual(len(root.findall('student')), 2)

    def test_student_attrs_exist(self):
        root = build_xml_tree(self.data)
        for s in root.findall('student'):
            self.assertIn('id', s.attrib)
            self.assertIn('dept', s.attrib)
            self.assertIn('school', s.attrib)
            self.assertIn('zip', s.attrib)

    def test_empty_student_list(self):
        data = dict(self.data, 學生清單=[])
        root = build_xml_tree(data)
        self.assertEqual(root.attrib['total'], '0')
        self.assertEqual(len(root.findall('student')), 0)

    def test_xml_is_valid(self):
        root = build_xml_tree(self.data)
        xml_str = ET.tostring(root, encoding='unicode')
        parsed = ET.fromstring(xml_str)
        self.assertEqual(parsed.tag, 'students')
        self.assertEqual(len(parsed.findall('student')), 2)

    def test_student_values_correct(self):
        root = build_xml_tree(self.data)
        first = root.findall('student')[0]
        self.assertEqual(first.attrib['id'], 'S001')
        self.assertEqual(first.attrib['dept'], '資訊工程系')
        self.assertEqual(first.attrib['school'], '國立馬公高中')
        self.assertEqual(first.attrib['zip'], '880')


if __name__ == '__main__':
    unittest.main()
