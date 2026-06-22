import os
import sys
import unittest
import importlib.util

MODULE_PATH = os.path.join(os.path.dirname(__file__), "q3.py")
SPEC = importlib.util.spec_from_file_location("q3_solution", MODULE_PATH)
q3_solution = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(q3_solution)

digit_sum_in_base = q3_solution.digit_sum_in_base
digital_root_in_base = q3_solution.digital_root_in_base
solve = q3_solution.solve
to_base_digits = q3_solution.to_base_digits


class TestQ3DigitalRootInBase(unittest.TestCase):
    def test_zero_root_is_zero(self):
        self.assertEqual(to_base_digits(0, 6), [0])
        self.assertEqual(digital_root_in_base(0, 6), 0)

    def test_general_case_eight(self):
        self.assertEqual(to_base_digits(8, 6), [1, 2])
        self.assertEqual(digit_sum_in_base(8, 6), 3)
        self.assertEqual(digital_root_in_base(8, 6), 3)

    def test_general_case_sixty_three(self):
        self.assertEqual(to_base_digits(63, 6), [1, 4, 3])
        self.assertEqual(digit_sum_in_base(63, 6), 8)
        self.assertEqual(digital_root_in_base(63, 6), 3)

    def test_large_number(self):
        self.assertEqual(digital_root_in_base(1_000_000_000, 6), 5)

    def test_multiple_lines_until_eof(self):
        self.assertEqual(solve("0\n8\n63\n", 6), "0\n3\n3")

    def test_edge_invalid_base_raises(self):
        with self.assertRaises(ValueError):
            to_base_digits(10, 4)
        with self.assertRaises(ValueError):
            digital_root_in_base(-1, 6)


if __name__ == "__main__":
    unittest.main()
