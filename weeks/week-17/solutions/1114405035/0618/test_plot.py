import os
import unittest

from plot import generate_radar_chart


class TestPlot(unittest.TestCase):
    def setUp(self):
        self.data_path = "results.json"
        self.test_output_path = "assets/radar_test.png"

    def tearDown(self):
        if os.path.exists(self.test_output_path):
            try:
                os.remove(self.test_output_path)
            except OSError:
                pass

    def test_generate_radar_chart_success(self):
        if not os.path.exists(self.data_path):
            self.skipTest("results.json 尚未產生，跳過測試")
        generate_radar_chart(self.data_path, self.test_output_path)
        self.assertTrue(os.path.exists(self.test_output_path))
        self.assertGreater(os.path.getsize(self.test_output_path), 0)

    def test_missing_source_file_raises_error(self):
        with self.assertRaises(FileNotFoundError):
            generate_radar_chart("non_existent_file.json", self.test_output_path)


if __name__ == "__main__":
    unittest.main()
