import json
import os
import pickle
import tempfile
import unittest
from pathlib import Path

from stage3 import benchmark
from stage4 import plot


class TestSecurity(unittest.TestCase):
    def test_make_data_rejects_negative_count(self):
        with self.assertRaises(ValueError):
            benchmark.make_data(-1)

    def test_load_results_uses_json_not_pickle(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / 'results.json'
            with path.open('wb') as f:
                pickle.dump({'bubble_sort': {10: 0.1}}, f)

            with self.assertRaises((json.JSONDecodeError, ValueError)):
                plot.load_results(str(path))

    def test_load_results_normalizes_keys_to_int(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / 'results.json'
            data = {'bubble_sort': {'10': 0.1}, 'sorted': {'20': 0.05}}
            path.write_text(json.dumps(data), encoding='utf-8')

            loaded = plot.load_results(str(path))
            self.assertEqual(loaded['bubble_sort'], {10: 0.1})
            self.assertEqual(loaded['sorted'], {20: 0.05})

    def test_save_results_creates_json_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = Path(tmpdir) / 'results.json'
            results = {'bubble_sort': {5: 0.1}}
            benchmark.save_results(results, str(out_path))

            self.assertTrue(out_path.exists())
            loaded = plot.load_results(str(out_path))
            self.assertEqual(loaded, results)


if __name__ == '__main__':
    unittest.main()
