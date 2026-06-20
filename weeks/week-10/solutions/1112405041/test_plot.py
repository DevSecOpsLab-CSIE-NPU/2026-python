import unittest
import tempfile
import os
from task3_plot_comparison import plot_comparison

class TestPlot(unittest.TestCase):

    def test_plot_creates_file(self):
        data = {"read_csv": 0.002, "write_json": 0.001, "read_json": 0.0009, "write_xml": 0.003}
        out = tempfile.mktemp(suffix=".png")
        plot_comparison(data, out)
        self.assertTrue(os.path.exists(out))
        self.assertGreater(os.path.getsize(out), 0)
        os.unlink(out)
