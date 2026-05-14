"""R03-xml-parse.py 的單元測試。"""

from __future__ import annotations

import unittest

from support import load_module


class TestR03XmlParse(unittest.TestCase):
    """確認 XML 範例已整理成可驗證的解析函式。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module("R03-xml-parse.py")
        cls.root = cls.module.parse_xml(cls.module.XML_DATA)

    def test_parse_xml_returns_root_with_attributes(self):
        self.assertEqual("rss", self.root.tag)
        self.assertEqual("2.0", self.module.get_attribute(self.root, "version"))

    def test_can_extract_channel_title_and_items(self):
        title = self.module.get_channel_title(self.root)
        items = self.module.list_items(self.root)

        self.assertEqual("Planet Python", title)
        self.assertEqual(
            {"title": "討論 Python 型別提示", "link": "https://example.com/1", "author": "Alice"},
            items[0],
        )
        self.assertEqual(2, len(items))

    def test_iter_titles_and_missing_default(self):
        titles = self.module.list_titles(self.root)

        self.assertEqual(["Planet Python", "討論 Python 型別提示", "asyncio 最佳實踐"], titles)
        self.assertEqual("預設值", self.module.get_attribute(self.root, "missing", "預設值"))


if __name__ == "__main__":
    unittest.main()
