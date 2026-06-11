import os
import unittest

from plot import plot_benchmark


class TestPlot(unittest.TestCase):
    def test_generate_non_empty_png(self):
        output_path = "assets/benchmark.png"

        if os.path.exists(output_path):
            os.remove(output_path)

        plot_benchmark("results.json", output_path)

        self.assertTrue(os.path.exists(output_path))
        self.assertGreater(os.path.getsize(output_path), 0)


if __name__ == "__main__":
    unittest.main()
