import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from benchmark import make_data
from plot import load_results
from timing import timeit


class TestSecurityRules(unittest.TestCase):
    def test_make_data_rejects_negative_size(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_load_results_rejects_invalid_json_payload(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "results.json"
            path.write_bytes(b"not-json")

            with self.assertRaises((json.JSONDecodeError, UnicodeDecodeError)):
                load_results(str(path))

    def test_timeit_does_not_print(self):
        @timeit
        def sample():
            return "ok"

        with patch("builtins.print") as mocked_print:
            self.assertEqual(sample(), "ok")

        mocked_print.assert_not_called()


if __name__ == "__main__":
    unittest.main()