import pathlib
import sys
import unittest

THIS_FILE = pathlib.Path(__file__).resolve()
SOLUTION_DIR = THIS_FILE.parent.parent
sys.path.insert(0, str(SOLUTION_DIR))

from task1_sequence_clean import parse_input, process_numbers, format_output


class TestTask1(unittest.TestCase):
    def test_basic(self):
        nums = parse_input("5 3 5 2 9 2 8 3 1")
        out = process_numbers(nums)
        self.assertEqual(out["dedupe"], [5, 3, 2, 9, 8, 1])
        self.assertEqual(out["asc"], [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(out["desc"], [9, 8, 5, 5, 3, 3, 2, 2, 1])
        self.assertEqual(out["evens"], [2, 2, 8])

    def test_empty(self):
        nums = parse_input("")
        out = process_numbers(nums)
        self.assertEqual(out["dedupe"], [])
        self.assertEqual(out["asc"], [])
        self.assertEqual(out["desc"], [])
        self.assertEqual(out["evens"], [])

    def test_with_zero(self):
        nums = parse_input("-1 0 -2 0 3 -2")
        out = process_numbers(nums)
        self.assertEqual(out["dedupe"], [-1, 0, -2, 3])
        self.assertEqual(out["evens"], [0, -2, 0, -2])

    def test_format(self):
        data = {
            "dedupe": [1, 2],
            "asc": [1, 2, 2],
            "desc": [2, 2, 1],
            "evens": [2, 2],
        }
        text = format_output(data)
        self.assertIn("dedupe: 1 2", text)
        self.assertIn("asc: 1 2 2", text)
        self.assertIn("desc: 2 2 1", text)
        self.assertIn("evens: 2 2", text)


if __name__ == "__main__":
    unittest.main()