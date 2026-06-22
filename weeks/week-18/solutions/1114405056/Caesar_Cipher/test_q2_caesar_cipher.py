import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("q2_caesar_cipher.py")


class TestQ2CaesarCipher(unittest.TestCase):
    def run_program(self, text):
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input=text,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout

    def test_sample(self):
        data = "Hello, NPU!\nabc XYZ\n"
        self.assertEqual(self.run_program(data), "Olssp, WVE!\nhij efg\n")

    def test_wraparound(self):
        self.assertEqual(self.run_program("Zz Aa\n"), "Gf Hh\n")

    def test_non_letters_stay_same(self):
        self.assertEqual(self.run_program("123 !?,.-\n"), "123 !?,.-\n")


if __name__ == "__main__":
    unittest.main()
