import unittest
import json
import tempfile
import os
from task2_json_to_xml import read_json, JSONReadError

class TestReadJSON(unittest.TestCase):

    def test_read_json_normal(self):
        data = {"name": "test", "value": 123}
        tmp = tempfile.mktemp(suffix=".json")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f)
        result = read_json(tmp)
        self.assertEqual(result, data)
        os.unlink(tmp)

    def test_read_json_empty_dict(self):
        tmp = tempfile.mktemp(suffix=".json")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump({}, f)
        result = read_json(tmp)
        self.assertEqual(result, {})
        os.unlink(tmp)

    def test_read_json_malformed_raises(self):
        tmp = tempfile.mktemp(suffix=".json")
        with open(tmp, "w", encoding="utf-8") as f:
            f.write("這不是 json")
        with self.assertRaises(JSONReadError):
            read_json(tmp)
        os.unlink(tmp)

    def test_read_json_empty_file_raises(self):
        tmp = tempfile.mktemp(suffix=".json")
        with open(tmp, "w", encoding="utf-8") as f:
            f.write("")
        with self.assertRaises(JSONReadError):
            read_json(tmp)
        os.unlink(tmp)
