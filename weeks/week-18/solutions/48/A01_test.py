import unittest
from io import StringIO
import sys
from A01_easy import main

D = 2

def run_with_input(text):
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin = StringIO(text)
    sys.stdout = StringIO()
    try:
        main()
        return sys.stdout.getvalue()
    finally:
        sys.stdin, sys.stdout = old_in, old_out


class TestDataCleaningA01(unittest.TestCase):

    def test_sample_1(self):
        """4 7 4 2 9 2 6 7 → 2 4 6"""
        out = run_with_input("8\n4 7 4 2 9 2 6 7\n0\n")
        self.assertEqual(out.strip(), "2 4 6")

    def test_sample_2(self):
        """1 3 5 → 無偶數 → NONE"""
        out = run_with_input("3\n1 3 5\n0\n")
        self.assertEqual(out.strip(), "NONE")

    def test_all_even_with_duplicates(self):
        """全偶數含重複"""
        out = run_with_input("6\n2 4 2 6 4 8\n0\n")
        self.assertEqual(out.strip(), "2 4 6 8")

    def test_single_even(self):
        """單一偶數"""
        out = run_with_input("1\n-8\n0\n")
        self.assertEqual(out.strip(), "-8")

    def test_single_odd(self):
        """單一奇數 → NONE"""
        out = run_with_input("1\n7\n0\n")
        self.assertEqual(out.strip(), "NONE")

    def test_negative_even(self):
        """含負偶數"""
        out = run_with_input("2\n-4 6\n0\n")
        self.assertEqual(out.strip(), "-4 6")

    def test_multiple_groups(self):
        """多組測資"""
        out = run_with_input("8\n4 7 4 2 9 2 6 7\n3\n1 3 5\n0\n")
        self.assertEqual(out.strip().splitlines(), ["2 4 6", "NONE"])


if __name__ == "__main__":
    unittest.main()
