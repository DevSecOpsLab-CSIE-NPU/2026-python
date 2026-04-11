import unittest


def minimal_distance_sum(addresses):
    # 先排序，再選中位數，這樣總距離一定是最小的。
    ordered = sorted(addresses)
    median = ordered[len(ordered) // 2]
    return sum(abs(value - median) for value in ordered)


class TestUVA10041(unittest.TestCase):
    def test_sample_style_case(self):
        # 這組刻意放入重複與分散數值，檢查中位數選擇是否正確。
        self.assertEqual(minimal_distance_sum([2, 4, 6, 8, 10]), 12)

    def test_duplicate_addresses(self):
        # 所有人住同一條門牌時，總距離應該是 0。
        self.assertEqual(minimal_distance_sum([15, 15, 15, 15]), 0)

    def test_even_count_case(self):
        # 偶數個房子時，選擇任一中間值都可；這裡驗證我們的實作是否穩定。
        self.assertEqual(minimal_distance_sum([1, 2, 3, 4]), 4)


if __name__ == "__main__":
    unittest.main()