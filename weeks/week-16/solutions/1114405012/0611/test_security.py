import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from benchmark import make_data
from plot import load_results


class TestSecurity(unittest.TestCase):
    def test_make_data_rejects_negative(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_load_results_uses_json_file_and_handles_missing_file(self):
        with TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            missing_path = temp_path / "missing.json"
            with self.assertRaises(FileNotFoundError):
                load_results(str(missing_path))

    def test_load_results_reads_plain_json(self):
        with TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            results_path = temp_path / "results.json"
            results_path.write_text('{"500": {"sorted": 0.01}}', encoding="utf-8")
            results = load_results(str(results_path))
            self.assertEqual(results["500"]["sorted"], 0.01)


if __name__ == "__main__":
    unittest.main()
