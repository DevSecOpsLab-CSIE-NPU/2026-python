import tempfile
import unittest
from pathlib import Path

from benchmark import make_data
from plot import load_results


class TestSecurityRules(unittest.TestCase):
    def test_make_data_rejects_negative_n(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_load_results_rejects_non_json_suffix(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.pkl"
            path.write_text("not-json", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_results(str(path))

    def test_load_results_rejects_invalid_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.json"
            path.write_text("{bad-json", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_results(str(path))


if __name__ == "__main__":
    unittest.main()
