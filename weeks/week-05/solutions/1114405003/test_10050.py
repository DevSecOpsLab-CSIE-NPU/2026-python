import unittest


def hartal_days_lost(days, parties):
    # 使用集合避免同一天被多個政黨重複計算。
    lost_days = set()
    for hartal_parameter in parties:
        for day in range(hartal_parameter, days + 1, hartal_parameter):
            # 第 6、7 天分別對應星期五與星期六，這兩天不算工作天。
            if day % 7 not in (6, 0):
                lost_days.add(day)
    return len(lost_days)


class TestUVA10050(unittest.TestCase):
    def test_official_example(self):
        # 題目敘述中的範例。
        self.assertEqual(hartal_days_lost(14, [3, 4, 8]), 5)

    def test_all_working_days_hit(self):
        # 驗證同一天被多個政黨命中時不會重複計算。
        self.assertEqual(hartal_days_lost(10, [2, 3, 4]), 6)

    def test_single_party_every_day(self):
        # h = 1 代表每天都會罷工，但週末仍然要排除。
        self.assertEqual(hartal_days_lost(7, [1]), 5)


if __name__ == "__main__":
    unittest.main()