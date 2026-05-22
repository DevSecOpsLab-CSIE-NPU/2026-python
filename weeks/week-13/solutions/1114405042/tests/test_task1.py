import sys
import unittest
from pathlib import Path

# Add parent directory to sys.path so we can import the module
sys.path.insert(0, str(Path(__file__).parent.parent))

from task1_grouped_bar import load_year, get_top_depts

DATA_DIR = Path(__file__).parent.parent.parent.parent.parent.parent / "assets" / "stu-data"

class TestTask1(unittest.TestCase):
    def test_load_year_returns_dict(self):
        result = load_year(112, DATA_DIR)
        self.assertIsInstance(result, dict)
        if result:
            self.assertIsInstance(list(result.keys())[0], str)

    def test_load_year_counts_correct(self):
        result = load_year(112, DATA_DIR)
        # Using a popular dept as a check. 
        # Check if '資訊工程系' exists and >0 if it exists.
        if '資訊工程系' in result:
            self.assertIsInstance(result['資訊工程系'], int)
            self.assertGreater(result['資訊工程系'], 0)

    def test_load_year_total_positive(self):
        result = load_year(112, DATA_DIR)
        total = sum(result.values())
        self.assertGreater(total, 0)

    def test_get_top_depts_length(self):
        year_data = {
            112: load_year(112, DATA_DIR),
            113: load_year(113, DATA_DIR),
            114: load_year(114, DATA_DIR)
        }
        depts = get_top_depts(year_data, top_n=8)
        self.assertGreaterEqual(len(depts), 8)
        self.assertLessEqual(len(depts), 24)

    def test_get_top_depts_includes_popular(self):
        year_data = {
            112: load_year(112, DATA_DIR)
        }
        depts = get_top_depts(year_data, top_n=8)
        top_dept_112 = sorted(year_data[112].items(), key=lambda x: x[1], reverse=True)[0][0]
        self.assertIn(top_dept_112, depts)

if __name__ == '__main__':
    unittest.main()
