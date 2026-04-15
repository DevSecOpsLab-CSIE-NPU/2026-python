import pathlib
import sys
import unittest

BASE_DIR = pathlib.Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from task1_sequence_clean import parse_numbers, dedupe_preserve_order, build_outputs


class TestTask1SequenceClean(unittest.TestCase):
    def test_normal_case(self):
        nums = parse_numbers("5 3 5 2 9 2 8 3 1")
        outputs = build_outputs(nums)
        self.assertEqual(outputs["dedupe"], [5, 3, 2, 9, 8, 1])
        self.assertEqual(outputs["asc"], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(outputs["desc"], [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(outputs["evens"], [2, 2, 8])

    def test_empty_input(self):
        nums = parse_numbers("")
        outputs = build_outputs(nums)
        self.assertEqual(outputs["dedupe"], [])
        self.assertEqual(outputs["asc"], [])
        self.assertEqual(outputs["desc"], [])
        self.assertEqual(outputs["evens"], [])

    def test_dedupe_order(self):
        self.assertEqual(dedupe_preserve_order([2, 1, 2, 1, 3]), [2, 1, 3])


if __name__ == "__main__":
    unittest.main()
