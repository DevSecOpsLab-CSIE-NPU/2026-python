import unittest
import os
from plot import plot_results, load_results

class TestPlot(unittest.TestCase):
    def setUp(self):
        self.dummy_results = {
            "baseline": {"500": 0.0001, "1000": 0.0002},
            "bubble_sort": {"500": 0.01, "1000": 0.04}
        }
        self.out_dir = "assets"
        self.out_path = os.path.join(self.out_dir, "test_benchmark.png")
        os.makedirs(self.out_dir, exist_ok=True)
        
    def tearDown(self):
        if os.path.exists(self.out_path):
            os.remove(self.out_path)

    def test_plot_generates_file(self):
        if os.path.exists(self.out_path):
            os.remove(self.out_path)
            
        plot_results(self.dummy_results, self.out_path)
        
        # 驗證 PNG 確實產生
        self.assertTrue(os.path.exists(self.out_path), "Plot file was not created")
        
        # 驗證檔案非空
        self.assertGreater(os.path.getsize(self.out_path), 0, "Plot file is empty")

if __name__ == '__main__':
    unittest.main()
