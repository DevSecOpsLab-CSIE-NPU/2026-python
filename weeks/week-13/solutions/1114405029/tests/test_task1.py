import unittest
from pathlib import Path
import sys

# 讓測試檔可以 import 上一層的 task1_grouped_bar.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from task1_grouped_bar import load_year, get_top_depts


class TestTask1GroupedBar(unittest.TestCase):
    """測試 Task 1：三年並排長條圖需要用到的資料處理函式。"""

    def setUp(self):
        """
        找到 week-13 目錄，
        再進入 assets/stu-data。
        """

        # test_task1.py
        # → tests
        # → 1114405029
        # → solutions
        # → week-13
        self.base_dir = Path(__file__).resolve().parents[5]

        # 組合資料夾路徑
        self.data_dir = self.base_dir / "assets" / "stu-data"

    def test_load_year_returns_dict(self):
        """load_year() 應該回傳 dict，而且 key 應該是字串。"""

        result = load_year(114, self.data_dir)

        self.assertIsInstance(result, dict)
        self.assertTrue(
            all(isinstance(key, str) for key in result.keys())
        )

    def test_load_year_counts_correct(self):
        """
        驗證已知資料：
        114 年觀光休閒系招生人數應為 58 人。
        """

        result = load_year(114, self.data_dir)

        self.assertEqual(result["觀光休閒系"], 58)

    def test_load_year_total_positive(self):
        """單一年份總招生人數應該大於 0。"""

        result = load_year(114, self.data_dir)

        self.assertGreater(sum(result.values()), 0)

    def test_get_top_depts_length(self):
        """get_top_depts() 回傳數量不應超過合理範圍。"""

        year_data = {
            112: load_year(112, self.data_dir),
            113: load_year(113, self.data_dir),
            114: load_year(114, self.data_dir),
        }

        result = get_top_depts(year_data, top_n=8)

        # 三年 union 後理論上最多 24 個
        self.assertLessEqual(len(result), 24)

    def test_get_top_depts_includes_popular(self):
        """熱門系所應該出現在結果中。"""

        year_data = {
            112: load_year(112, self.data_dir),
            113: load_year(113, self.data_dir),
            114: load_year(114, self.data_dir),
        }

        result = get_top_depts(year_data, top_n=8)

        self.assertIn("觀光休閒系", result)


if __name__ == "__main__":
    unittest.main()