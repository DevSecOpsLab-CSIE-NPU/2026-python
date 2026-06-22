import unittest
from io import StringIO
import sys
from B13_easy import main

def run_with_input(text):
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin = StringIO(text)
    sys.stdout = StringIO()
    try:
        main()
        return sys.stdout.getvalue()
    finally:
        sys.stdin, sys.stdout = old_in, old_out


class TestBase13DigitalRoot(unittest.TestCase):

    def test_input_0(self):
        """題目範例：0 → 0"""
        out = run_with_input("0\n")
        self.assertEqual(out.strip(), "0")

    def test_input_8(self):
        """題目範例：8 → 8"""
        out = run_with_input("8\n")
        self.assertEqual(out.strip(), "8")

    def test_input_63(self):
        """題目範例：63 → 3"""
        out = run_with_input("63\n")
        self.assertEqual(out.strip(), "3")

    def test_input_13(self):
        """13(10) = 10(13) → 1+0=1"""
        out = run_with_input("13\n")
        self.assertEqual(out.strip(), "1")

    def test_input_169(self):
        """169(10) = 100(13) → 1+0+0=1"""
        out = run_with_input("169\n")
        self.assertEqual(out.strip(), "1")

    def test_input_12(self):
        """12(10) = 12(13) → 12 < 13，不動"""
        out = run_with_input("12\n")
        self.assertEqual(out.strip(), "12")

    def test_input_25(self):
        """25(10) = 1,12(13) → 1+12=13 → 13(10)=1,0(13) → 1+0=1"""
        out = run_with_input("25\n")
        self.assertEqual(out.strip(), "1")

    def test_input_170(self):
        """170(10) = 101(13) → 1+0+1=2"""
        out = run_with_input("170\n")
        self.assertEqual(out.strip(), "2")

    def test_multiple_lines(self):
        """多行測資"""
        out = run_with_input("0\n8\n63\n13\n")
        self.assertEqual(out.strip().splitlines(), ["0", "8", "3", "1"])


if __name__ == "__main__":
    unittest.main()
