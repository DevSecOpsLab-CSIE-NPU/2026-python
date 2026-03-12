import unittest

from task1_sequence_clean import dedupe_preserve_order, solve


class TestTask1SequenceClean(unittest.TestCase):
    def test_dedupe_preserves_first_occurrence(self):
        numbers = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        self.assertEqual(dedupe_preserve_order(numbers), [5, 3, 2, 9, 8, 1])

    def test_solve_formats_expected_output(self):
        raw = "5 3 5 2 9 2 8 3 1"
        expected = "\n".join(
            [
                "dedupe: 5 3 2 9 8 1",
                "asc: 1 2 2 3 3 5 5 8 9",
                "desc: 9 8 5 5 3 3 2 2 1",
                "evens: 2 2 8",
            ]
        )
        self.assertEqual(solve(raw), expected)

    def test_empty_input_returns_empty_sections(self):
        expected = "\n".join(
            [
                "dedupe:",
                "asc:",
                "desc:",
                "evens:",
            ]
        )
        self.assertEqual(solve(""), expected)


if __name__ == "__main__":
    unittest.main()
