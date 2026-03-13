import unittest

from task1_sequence_clean import build_report, dedupe_keep_order, parse_numbers_line


class TestTask1(unittest.TestCase):
    def test_parse_numbers_line_empty(self):
        self.assertEqual(parse_numbers_line("   "), [])

    def test_dedupe_keep_first_order(self):
        self.assertEqual(dedupe_keep_order([5, 3, 5, 2, 3]), [5, 3, 2])

    def test_build_report_normal_case(self):
        report = build_report([5, 3, 5, 2, 9, 2, 8, 3, 1])
        self.assertEqual(report["dedupe"], [5, 3, 2, 9, 8, 1])
        self.assertEqual(report["asc"], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(report["desc"], [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(report["evens"], [2, 2, 8])


if __name__ == "__main__":
    unittest.main()
