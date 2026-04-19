import unittest

from task1_sequence_clean import dedupe_preserve_order, filter_evens, solve, sort_ascending, sort_descending


class Task1SequenceCleanTests(unittest.TestCase):
    def test_dedupe_preserves_first_occurrence(self):
        self.assertEqual(dedupe_preserve_order([5, 3, 5, 2, 3, 1]), [5, 3, 2, 1])

    def test_sort_ascending_keeps_duplicates(self):
        self.assertEqual(sort_ascending([5, 3, 5, 2]), [2, 3, 5, 5])

    def test_filter_evens_keeps_original_order(self):
        self.assertEqual(filter_evens([5, 2, 8, 3, 2]), [2, 8, 2])

    def test_sort_descending_orders_all_values(self):
        self.assertEqual(sort_descending([5, 3, 5, 2]), [5, 5, 3, 2])

    def test_solve_formats_sample_output(self):
        text = "5 3 5 2 9 2 8 3 1\n"
        expected = "dedupe: 5 3 2 9 8 1\nasc: 1 2 2 3 3 5 5 8 9\ndesc: 9 8 5 5 3 3 2 2 1\nevens: 2 2 8"
        self.assertEqual(solve(text), expected)


if __name__ == "__main__":
    unittest.main()