import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import benchmark
from benchmark import load_results, make_data, run_benchmark, save_results


class TestSecurityPractices(unittest.TestCase):
    def test_make_data_rejects_negative_size(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_run_benchmark_rejects_invalid_queries(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(10,), queries=0)

    def test_results_use_json_not_pickle(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.json"
            save_results({"rows": []}, path)

            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), {"rows": []})
            with patch.object(benchmark, "json", wraps=json) as json_mock:
                self.assertEqual(load_results(path), {"rows": []})
                self.assertTrue(json_mock.load.called)


if __name__ == "__main__":
    unittest.main()
