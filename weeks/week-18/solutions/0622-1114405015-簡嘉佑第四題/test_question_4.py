import unittest

from question_4_solution import (
    K,
    binary_search,
    faster_label,
    format_search_result,
    linear_search,
    parse_or_generate_array,
)


class TestQuestion4(unittest.TestCase):
    def test_linear_found(self):
        arr = [1, 3, 5, 7, 9]
        idx, cmp_count = linear_search(arr, 7)
        self.assertEqual(idx, 3)
        self.assertEqual(cmp_count, 4)

    def test_linear_not_found(self):
        arr = [2, 4, 6]
        idx, cmp_count = linear_search(arr, 5)
        self.assertEqual(idx, -1)
        self.assertEqual(cmp_count, 3)

    def test_binary_found(self):
        arr = [10, 20, 30, 40, 50]
        idx, cmp_count = binary_search(arr, 40)
        self.assertEqual(idx, 3)
        self.assertGreaterEqual(cmp_count, 1)

    def test_binary_not_found(self):
        arr = [10, 20, 30, 40, 50]
        idx, cmp_count = binary_search(arr, 35)
        self.assertEqual(idx, -1)
        self.assertGreaterEqual(cmp_count, 1)

    def test_parse_input_mode(self):
        lines = ["5\n", "1 4 7 115 300\n"]
        arr = parse_or_generate_array(lines)
        self.assertEqual(arr, [1, 4, 7, 115, 300])

    def test_parse_auto_generate(self):
        arr = parse_or_generate_array([], default_size=8)
        self.assertEqual(arr, [0, 1, 2, 3, 4, 5, 6, 7])

    def test_result_format(self):
        self.assertEqual(format_search_result(9, 4), "FOUND 9 cmp=4")
        self.assertEqual(format_search_result(-1, 7), "NOT FOUND cmp=7")

    def test_faster_label(self):
        self.assertEqual(faster_label(0.1, 0.2), "linear faster")
        self.assertEqual(faster_label(0.3, 0.2), "binary faster")
        self.assertEqual(faster_label(0.2, 0.2), "tie")

    def test_target_constant(self):
        self.assertEqual(K, 115)


if __name__ == "__main__":
    unittest.main(verbosity=2)
