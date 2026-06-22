import os
import sys
import unittest
import importlib.util

MODULE_PATH = os.path.join(os.path.dirname(__file__), "q2.py")
SPEC = importlib.util.spec_from_file_location("q2_solution", MODULE_PATH)
q2_solution = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(q2_solution)

caesar_line = q2_solution.caesar_line
shift_char = q2_solution.shift_char
solve = q2_solution.solve


class TestQ2CaesarCipher(unittest.TestCase):
    def test_mixed_case_letters(self):
        self.assertEqual(caesar_line("Hello, NPU!", 10), "Rovvy, XZE!")

    def test_wraparound_for_z_and_upper_z(self):
        self.assertEqual(shift_char("z", 10), "j")
        self.assertEqual(shift_char("Z", 10), "J")
        self.assertEqual(caesar_line("abc XYZ", 10), "klm HIJ")

    def test_punctuation_spaces_and_digits_unchanged(self):
        self.assertEqual(caesar_line("Room 101: A+B?", 10), "Byyw 101: K+L?")

    def test_multiple_lines_until_eof(self):
        text = "Hello, NPU!\nabc XYZ\n"
        self.assertEqual(solve(text, 10), "Rovvy, XZE!\nklm HIJ")

    def test_edge_empty_line_is_preserved(self):
        self.assertEqual(solve("\nABC\n", 10), "\nKLM")

    def test_shift_larger_than_alphabet(self):
        self.assertEqual(caesar_line("Az", 36), "Kj")


if __name__ == "__main__":
    unittest.main()
