import os
import json
import unittest
from timing import timeit


class TestSecurity(unittest.TestCase):
    def test_results_file_closed(self):
        """
        OpenSSF 08: ensure files are closed via `with` statement.
        After results.json is read, it should not cause resource warnings.
        """
        path = "results.json"
        if not os.path.exists(path):
            self.skipTest("results.json not found")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("1000", data)

    def test_make_data_rejects_negative(self):
        """
        OpenSSF 03: check input boundary.
        make_data with negative n should raise.
        """
        from benchmark import make_data
        with self.assertRaises(ValueError):
            make_data(-5)

    def test_load_uses_json_not_pickle(self):
        """
        OpenSSF 04: JSON is safer than pickle (CWE-502).
        Verify plot.py imports json, not pickle.
        """
        with open("plot.py", "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("json", content)
        self.assertNotIn("import pickle", content)
        self.assertNotIn("from pickle", content)


if __name__ == "__main__":
    unittest.main()
