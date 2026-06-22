import io
import unittest
from unittest.mock import patch

import main


class TestDataCleaningProgram(unittest.TestCase):
    def run_program(self, input_text):
        fake_stdout = io.StringIO()
        with patch("sys.stdin", io.StringIO(input_text)), patch("sys.stdout", fake_stdout):
            main.main()
        return fake_stdout.getvalue()

    def test_normal_case_removes_duplicates_filters_multiples_of_5_and_sorts(self):
        input_text = """8
10 3 5 10 20 7 5 15
0
"""
        expected = """5 10 15 20
"""
        self.assertEqual(self.run_program(input_text), expected)

    def test_boundary_case_single_valid_number(self):
        input_text = """1
5
0
"""
        expected = """5
"""
        self.assertEqual(self.run_program(input_text), expected)

    def test_special_case_outputs_none_when_no_number_matches(self):
        input_text = """4
1 2 3 4
0
"""
        expected = """NONE
"""
        self.assertEqual(self.run_program(input_text), expected)

    def test_edge_case_handles_negative_numbers_zero_and_duplicates(self):
        input_text = """7
-10 0 -10 25 12 0 -5
0
"""
        expected = """-10 -5 0 25
"""
        self.assertEqual(self.run_program(input_text), expected)


if __name__ == "__main__":
    unittest.main()
