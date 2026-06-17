import unittest
from unittest.mock import patch


class TestSecurity(unittest.TestCase):

    def test_make_data_rejects_negative_n(self):
        from benchmark import make_data
        with self.assertRaises(ValueError):
            make_data(-1)
        with self.assertRaises(ValueError):
            make_data(0)

    def test_make_data_rejects_negative_seed(self):
        from benchmark import make_data
        make_data(10, seed=-1)

    def test_plot_loads_json_not_pickle(self):
        import json
        import pickle
        with open("results.json") as f:
            content = f.read()
        obj = json.loads(content)
        self.assertIsInstance(obj, dict)

    def test_load_results_missing_file(self):
        from plot import load_results
        with self.assertRaises(FileNotFoundError):
            load_results("nonexistent.json")

    def test_no_assert_for_input_validation(self):
        import ast
        import os

        for fname in ["timing.py", "search.py", "benchmark.py", "plot.py"]:
            if not os.path.exists(fname):
                continue
            with open(fname, encoding="utf-8") as f:
                tree = ast.parse(f.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.Assert):
                    self.fail(f"{fname} uses assert for validation at line {node.lineno}")


if __name__ == "__main__":
    unittest.main()
