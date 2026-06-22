import unittest
import sys
import io
from A03 import digit_root_in_base, main


class TestDigitRootInBase(unittest.TestCase):

    def test_zero(self):
        """x=0 -> 0"""
        self.assertEqual(digit_root_in_base(0, base=8), 0)

    def test_single_digit_less_than_base(self):
        """一位數且<base -> 本身"""
        self.assertEqual(digit_root_in_base(5, base=8), 5)

    def test_exactly_base(self):
        """剛好等於base: 8 -> octal 10 -> 1+0=1"""
        self.assertEqual(digit_root_in_base(8, base=8), 1)

    def test_two_layer(self):
        """63 -> octal 77 -> 14 -> octal 16 -> 1+6=7"""
        self.assertEqual(digit_root_in_base(63, base=8), 7)

    def test_large_number(self):
        """1000 -> octal 1750 -> 1+7+5+0=13 -> octal 15 -> 1+5=6"""
        self.assertEqual(digit_root_in_base(1000, base=8), 6)

    def test_main_output(self):
        """主程式多行輸出"""
        sys.stdin = io.StringIO("0\n8\n63\n")
        sys.stdout = io.StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "0\n1\n7")


if __name__ == "__main__":
    unittest.main()
