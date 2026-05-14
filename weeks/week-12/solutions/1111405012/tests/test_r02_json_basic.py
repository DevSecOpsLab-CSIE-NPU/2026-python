"""R02-json-basic.py 的單元測試。"""

from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from support import load_module


class TestR02JsonBasic(unittest.TestCase):
    """確認 JSON 範例已整理成可測試的序列化工具。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module("R02-json-basic.py")

    def test_json_round_trip_preserves_data(self):
        json_text = self.module.to_json_text(self.module.SAMPLE_DATA)
        restored = self.module.from_json_text(json_text)

        self.assertEqual(self.module.SAMPLE_DATA, restored)

    def test_pretty_json_can_sort_keys(self):
        json_text = self.module.to_json_text({"b": 1, "a": 2}, indent=2, sort_keys=True)

        self.assertLess(json_text.find('"a"'), json_text.find('"b"'))
        self.assertIn("\n", json_text)

    def test_write_and_read_json_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "sample.json"
            self.module.write_json_file(self.module.SAMPLE_DATA, file_path)
            loaded = self.module.read_json_file(file_path)

        self.assertEqual(self.module.SAMPLE_DATA, loaded)

    def test_ensure_ascii_switches_chinese_output(self):
        record = {"城市": "澎湖"}
        escaped = self.module.to_json_text(record, ensure_ascii=True)
        utf8_text = self.module.to_json_text(record, ensure_ascii=False)

        self.assertIn("\\u57ce\\u5e02", escaped)
        self.assertIn("澎湖", utf8_text)


if __name__ == "__main__":
    unittest.main()
