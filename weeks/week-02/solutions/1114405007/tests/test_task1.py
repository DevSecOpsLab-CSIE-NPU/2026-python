import unittest

from task1_sequence_clean import clean_sequence, dedupe_preserve_order


class TestTask1(unittest.TestCase):
    def test_dedupe_preserve_order_keeps_first_occurrence(self) -> None:
        self.assertEqual(dedupe_preserve_order([5, 3, 5, 2, 9, 2]), [5, 3, 2, 9])

    def test_clean_sequence_example_case(self) -> None:
        result = clean_sequence([5, 3, 5, 2, 9, 2, 8, 3, 1])
        self.assertEqual(result["dedupe"], [5, 3, 2, 9, 8, 1])
        self.assertEqual(result["asc"], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(result["desc"], [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(result["evens"], [2, 2, 8])

    def test_clean_sequence_empty_input(self) -> None:
        result = clean_sequence([])
        self.assertEqual(result, {"dedupe": [], "asc": [], "desc": [], "evens": []})


if __name__ == "__main__":
    unittest.main()
