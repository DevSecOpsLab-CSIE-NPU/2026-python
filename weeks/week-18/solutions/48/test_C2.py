import unittest
from io import StringIO
import sys
from C2_easy import main

def run_with_input(input_text):
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(input_text)
    sys.stdout = StringIO()
    try:
        main()
        return sys.stdout.getvalue()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

class TestC2CaesarCipher(unittest.TestCase):

    def test_sample(self):
        output = run_with_input("Hello, NPU!\nabc XYZ\n")
        self.assertEqual(output.strip(), "Qnuux, WYD!\njkl GHI")

    def test_empty_string(self):
        output = run_with_input("\n")
        self.assertEqual(output.strip(), "")

    def test_non_alpha_only(self):
        output = run_with_input("123 !@#\n")
        self.assertEqual(output.strip(), "123 !@#")

    def test_lowercase_wrap(self):
        output = run_with_input("z\n")
        expected = chr((ord('z') - ord('a') + 9) % 26 + ord('a'))
        self.assertEqual(output.strip(), expected)

    def test_uppercase_wrap(self):
        output = run_with_input("Z\n")
        expected = chr((ord('Z') - ord('A') + 9) % 26 + ord('A'))
        self.assertEqual(output.strip(), expected)

if __name__ == "__main__":
    unittest.main()
