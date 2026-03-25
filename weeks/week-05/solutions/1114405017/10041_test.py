import unittest

def calculate_min_distance(streets):
    """計算最小總距離的核心邏輯"""
    if not streets:
        return 0
    streets.sort()
    median = streets[len(streets) // 2]
    return sum(abs(s - median) for s in streets)

class TestVitoFamily(unittest.TestCase):

    def test_example_1(self):
        # 範例測試：2 4 6 -> 中位數 4 -> |2-4| + |4-4| + |6-4| = 2 + 0 + 2 = 4
        self.assertEqual(calculate_min_distance([2, 4, 6]), 4)

    def test_example_2(self):
        # 範例測試：3 10 20 -> 中位數 10 -> |3-10| + |10-10| + |20-10| = 7 + 0 + 10 = 17
        self.assertEqual(calculate_min_distance([3, 10, 20]), 17)

    def test_same_addresses(self):
        # 測試相同門牌號碼的情況
        self.assertEqual(calculate_min_distance([5, 5, 5, 5]), 0)

    def test_even_count(self):
        # 測試偶數個親戚的情況：1, 10, 20, 30 -> 中位數選 20 或 10 皆可
        # 選 20: |1-20| + |10-20| + |20-20| + |30-20| = 19 + 10 + 0 + 10 = 39
        self.assertEqual(calculate_min_distance([1, 10, 20, 30]), 39)

    def test_single_relative(self):
        # 測試只有一個親戚的情況
        self.assertEqual(calculate_min_distance([100]), 0)

if __name__ == '__main__':
    unittest.main()