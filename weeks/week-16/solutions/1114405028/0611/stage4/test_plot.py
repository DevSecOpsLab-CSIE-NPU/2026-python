import json
import os
import tempfile
import unittest
from pathlib import Path

from stage4 import plot


class TestPlot(unittest.TestCase):
    def test_load_results_reads_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / 'results.json'
            expected = {'bubble_sort': {10: 0.1}}
            path.write_text(json.dumps(expected), encoding='utf-8')

            loaded = plot.load_results(str(path))
            self.assertEqual(loaded, expected)

    def test_plot_results_creates_png(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = Path(tmpdir) / 'benchmark.png'
            results = {'bubble_sort': {1: 0.01}, 'sorted': {1: 0.001}}

            plot.plot_results(results, str(out_path))
            self.assertTrue(out_path.exists())
            self.assertGreater(out_path.stat().st_size, 0)

    def test_plot_results_creates_output_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out_dir = Path(tmpdir) / 'assets' / 'plots'
            out_path = out_dir / 'benchmark.png'
            results = {'bubble_sort': {0: 0.0}, 'sorted': {0: 0.0}}

            plot.plot_results(results, str(out_path))
            self.assertTrue(out_path.exists())
            self.assertGreater(out_path.stat().st_size, 0)
            self.assertTrue(out_dir.exists())


if __name__ == '__main__':
    unittest.main()
