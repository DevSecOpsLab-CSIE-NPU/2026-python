import unittest
from benchmark import make_data
from plot import load_results


class TestSecurity(unittest.TestCase):
    def test_make_data_rejects_negative(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_load_results_rejects_invalid_json(self):
        import tempfile
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("not json")
            path = f.name
        with self.assertRaises(ValueError):
            load_results(path)

    def test_load_uses_json_not_pickle(self):
        import inspect
        import plot
        source = inspect.getsource(plot.load_results)
        self.assertIn("json.load", source)
        self.assertNotIn("pickle", source)
