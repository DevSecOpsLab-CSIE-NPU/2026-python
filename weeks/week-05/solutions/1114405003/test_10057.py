import unittest


def median_summary(numbers):
    # 先排序，再找左中位數與右中位數。
    ordered = sorted(numbers)
    middle_left = ordered[(len(ordered) - 1) // 2]
    middle_right = ordered[len(ordered) // 2]
    count = ordered.count(middle_left)
    possible_values = middle_right - middle_left + 1
    return middle_left, count, possible_values


class TestUVA10057(unittest.TestCase):
    def test_odd_length_case(self):
        # 奇數長度時，中位數只有一個值。
        self.assertEqual(median_summary([3, 1, 2, 2, 4]), (2, 2, 1))

    def test_even_length_case(self):
        # 偶數長度時，最小中位數、該值出現次數、可行中位數數量都要檢查。
        self.assertEqual(median_summary([1, 2, 3, 4]), (2, 1, 2))

    def test_all_same_numbers(self):
        # 全部數字相同時，答案應該非常直觀。
        self.assertEqual(median_summary([7, 7, 7, 7, 7, 7]), (7, 6, 1))


if __name__ == "__main__":
    unittest.main()