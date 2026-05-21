import unittest
from pathlib import Path
import sys

# 讓測試檔可以 import 主程式
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from task2_zipcode_heatmap import (
    zip_to_county,
    load_county_counts,
    get_top_counties,
)


class TestTask2Heatmap(unittest.TestCase):
    """測試 Task 2：郵遞區號熱力圖資料處理函式。"""

    def setUp(self):
        """
        找到 repo 根目錄，
        再進入 assets/stu-data。
        """

        self.base_dir = Path(__file__).resolve().parents[5]
        self.data_dir = self.base_dir / "assets" / "stu-data"

    def test_zip_to_county_penghu(self):
        """880 應該對應到澎湖縣。"""

        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        """未知郵遞區號應回傳「其他」。"""

        self.assertEqual(zip_to_county("999"), "其他")

    def test_load_county_counts_type(self):
        """load_county_counts() 應回傳 dict。"""

        result = load_county_counts(114, self.data_dir)

        self.assertIsInstance(result, dict)

    def test_load_county_counts_penghu_positive(self):
        """澎湖縣招生人數應大於 0。"""

        result = load_county_counts(114, self.data_dir)

        self.assertGreater(result["澎湖縣"], 0)

    def test_get_top_counties_length(self):
        """get_top_counties() 回傳數量不應超過 top_n。"""

        year_data = {
            109: load_county_counts(109, self.data_dir),
            110: load_county_counts(110, self.data_dir),
            111: load_county_counts(111, self.data_dir),
            112: load_county_counts(112, self.data_dir),
            113: load_county_counts(113, self.data_dir),
            114: load_county_counts(114, self.data_dir),
        }

        result = get_top_counties(year_data, top_n=10)

        self.assertLessEqual(len(result), 10)


if __name__ == "__main__":
    unittest.main()