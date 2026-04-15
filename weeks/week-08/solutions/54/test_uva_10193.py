import math
import unittest

from test_utils import load_module, run_script


class TestUVA10193(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10193.py")
        cls.easy = load_module("uva_10193-easy.py")

    def test_known_cases(self) -> None:
        raw_input = "2\n1010\n1100\n1000\n0101\n"
        expected = "Pair #1: All you need is love!\nPair #2: Love is not all you need!"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_gcd_logic(self) -> None:
        self.assertTrue(self.standard.is_love("10", "110"))
        self.assertFalse(self.standard.is_love("1", "10"))
        self.assertEqual(math.gcd(int("1010", 2), int("1100", 2)), 2)

    def test_command_line_execution(self) -> None:
        raw_input = "1\n10\n11\n"
        expected = "Pair #1: Love is not all you need!"
        self.assertEqual(run_script("uva_10193.py", raw_input), expected)


if __name__ == "__main__":
    unittest.main()
