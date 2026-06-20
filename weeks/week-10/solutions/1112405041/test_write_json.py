import unittest
import json
import tempfile
import os
from task1_csv_to_json import write_json

class TestWriteJSON(unittest.TestCase):

    def test_write_json_normal(self):
        data = {"a": 1, "b": 2}
        tmp = tempfile.mktemp(suffix=".json")
        write_json(data, tmp)
        with open(tmp, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        self.assertEqual(loaded, data)
        os.unlink(tmp)

    def test_write_json_empty_dict(self):
        data = {}
        tmp = tempfile.mktemp(suffix=".json")
        write_json(data, tmp)
        with open(tmp, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        self.assertEqual(loaded, {})
        os.unlink(tmp)

    def test_write_json_auto_creates_dir(self):
        data = {"x": 1}
        tmp = tempfile.mktemp(suffix=".json")
        subdir = tmp + "_dir"
        path = os.path.join(subdir, "test.json")
        write_json(data, path)
        self.assertTrue(os.path.exists(path))
        with open(path, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        self.assertEqual(loaded, data)
        os.unlink(path)
        os.rmdir(subdir)

    def test_write_json_output_valid(self):
        data = {"students": []}
        tmp = tempfile.mktemp(suffix=".json")
        write_json(data, tmp)
        with open(tmp, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        self.assertIsInstance(loaded, dict)
        os.unlink(tmp)
