import unittest
from io import StringIO
import sys

import main


class TestSequenceProcessor(unittest.TestCase):
    def test_sample_input(self):
        input_data = "8\n4 7 4 2 9 2 6 7\n3\n1 3 5\n0\n"
        sys.stdin = StringIO(input_data)
        out = StringIO()
        sys.stdout = out
        main.main()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue().strip(), "6 9\n3")

    def test_none_case(self):
        input_data = "4\n1 2 4 5\n0\n"
        sys.stdin = StringIO(input_data)
        out = StringIO()
        sys.stdout = out
        main.main()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue().strip(), "NONE")

    def test_negative_numbers(self):
        input_data = "4\n-3 -6 2 4\n0\n"
        sys.stdin = StringIO(input_data)
        out = StringIO()
        sys.stdout = out
        main.main()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue().strip(), "-6 -3")

    def test_all_same(self):
        input_data = "5\n3 3 3 3 3\n0\n"
        sys.stdin = StringIO(input_data)
        out = StringIO()
        sys.stdout = out
        main.main()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue().strip(), "3")

    def test_multiple_groups(self):
        input_data = "5\n3 3 3 3 3\n3\n6 3 9\n4\n1 2 4 5\n0\n"
        sys.stdin = StringIO(input_data)
        out = StringIO()
        sys.stdout = out
        main.main()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue().strip(), "3\n3 6 9\nNONE")


if __name__ == "__main__":
    unittest.main()
