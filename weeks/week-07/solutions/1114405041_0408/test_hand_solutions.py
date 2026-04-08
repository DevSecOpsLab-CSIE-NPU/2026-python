import unittest

from test_utils import load_module, run_script


class TestHandSolutions(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.uva_10062 = load_module("uva_10062-hand.py")
        cls.uva_10071 = load_module("uva_10071-hand.py")
        cls.uva_10093 = load_module("uva_10093-hand.py")
        cls.uva_10101 = load_module("uva_10101-hand.py")
        cls.uva_10170 = load_module("uva_10170-hand.py")

    def test_uva_10062(self) -> None:
        self.assertEqual(self.uva_10062.solve("AAABBC\n"), "67 1\n66 2\n65 3")
        self.assertEqual(run_script("uva_10062-hand.py", "Aab\n"), "98 1\n97 1\n65 1")

    def test_uva_10071(self) -> None:
        self.assertEqual(self.uva_10071.solve("0 0\n1 2\n-1 2\n"), "0\n4\n-4")
        self.assertEqual(run_script("uva_10071-hand.py", "3 7\n"), "42")

    def test_uva_10093(self) -> None:
        self.assertEqual(self.uva_10093.solve("1\nA\nZZ\n"), "2\n11\n36")
        self.assertEqual(run_script("uva_10093-hand.py", "A\n"), "11")

    def test_uva_10101(self) -> None:
        raw_input = "0\n1\n10000000\n123456789\n"
        expected = "   1. 0\n   2. 1\n   3. 1 kuti\n   4. 12 kuti 34 lakh 56 hajar 7 shata 89"
        self.assertEqual(self.uva_10101.solve(raw_input), expected)
        self.assertEqual(run_script("uva_10101-hand.py", "100000000\n"), "   1. 10 kuti")

    def test_uva_10170(self) -> None:
        self.assertEqual(self.uva_10170.solve("3 10\n1 1\n4 4\n"), "5\n1\n4")
        self.assertEqual(run_script("uva_10170-hand.py", "3 10\n"), "5")


if __name__ == "__main__":
    unittest.main()