"""R05-stats-counter.py 的單元測試。"""

from __future__ import annotations

import unittest

from support import load_module


class TestR05StatsCounter(unittest.TestCase):
    """確認 Counter / defaultdict / namedtuple 的整合範例。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module("R05-stats-counter.py")

    def test_counter_counts_words_and_can_merge(self):
        counter = self.module.count_words(self.module.WORDS)
        merged = self.module.merge_word_counts(counter, ["banana", "cherry"])

        self.assertEqual(3, counter["apple"])
        self.assertEqual(("apple", 3), counter.most_common(1)[0])
        self.assertEqual(3, merged["banana"])

    def test_group_members_by_department(self):
        grouped = self.module.group_members_by_dept(self.module.RECORDS)

        self.assertEqual(["Alice", "Carol", "Eve"], grouped["系資"])
        self.assertEqual(["Bob", "David"], grouped["電子"])

    def test_sum_scores_by_name(self):
        totals = self.module.sum_scores_by_name(self.module.SCORES)

        self.assertEqual({"Alice": 175, "Bob": 150}, totals)

    def test_calculate_department_averages(self):
        averages = self.module.calculate_dept_averages(self.module.DEPT_SCORE_ROWS)

        self.assertEqual({"系資": 88.5, "電子": 83.0}, averages)
        stock = self.module.make_stock("AA", 39.48, -0.18)
        self.assertEqual("AA", stock.symbol)


if __name__ == "__main__":
    unittest.main()
