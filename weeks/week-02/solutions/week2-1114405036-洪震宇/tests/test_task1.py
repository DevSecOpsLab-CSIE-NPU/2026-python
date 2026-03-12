import unittest

from task1_sequence_clean import format_sequence_clean, sequence_clean


class TestTask1SequenceClean(unittest.TestCase):
    def test_example_input(self):
        line = "5 3 5 2 9 2 8 3 1"
        deduped, asc, desc, evens = sequence_clean(line)
        self.assertEqual(deduped, [5, 3, 2, 9, 8, 1])
        self.assertEqual(asc, [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(desc, [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(evens, [2, 2, 8])

    def test_empty_input(self):
        deduped, asc, desc, evens = sequence_clean("")
        self.assertEqual(deduped, [])
        self.assertEqual(asc, [])
        self.assertEqual(desc, [])
        self.assertEqual(evens, [])

    def test_negative_and_duplicates(self):
        line = "-1 -1 0 2 -1 2"
        deduped, asc, desc, evens = sequence_clean(line)
        self.assertEqual(deduped, [-1, 0, 2])
        self.assertEqual(asc, [-1, -1, -1, 0, 2, 2])
        self.assertEqual(desc, [2, 2, 0, -1, -1, -1])
        self.assertEqual(evens, [0, 2, 2])

    def test_format_output(self):
        out = format_sequence_clean([1, 2], [1, 2], [2, 1], [2])
        expected = "dedupe: 1 2\nasc: 1 2\ndesc: 2 1\nevens: 2"
        self.assertEqual(out, expected)


if __name__ == "__main__":
    unittest.main()
