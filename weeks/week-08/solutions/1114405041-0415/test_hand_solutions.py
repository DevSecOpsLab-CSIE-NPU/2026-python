import unittest

from test_utils import load_module, run_script


class TestHandSolutions(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.uva_10189 = load_module("uva_10189-hand.py")
        cls.uva_10190 = load_module("uva_10190-hand.py")
        cls.uva_10193 = load_module("uva_10193-hand.py")
        cls.uva_10221 = load_module("uva_10221-hand.py")
        cls.uva_10222 = load_module("uva_10222-hand.py")

    def test_uva_10189(self) -> None:
        self.assertEqual(self.uva_10189.solve("1 1\n*\n0 0\n"), "Field #1:\n*")
        self.assertEqual(run_script("uva_10189-hand.py", "1 2\n..\n0 0\n"), "Field #1:\n00")

    def test_uva_10190(self) -> None:
        self.assertEqual(self.uva_10190.solve("27 3\n"), "27 9 3 1")
        self.assertEqual(run_script("uva_10190-hand.py", "7 7\n"), "7 1")

    def test_uva_10193(self) -> None:
        self.assertEqual(
            self.uva_10193.solve("1\n10\n110\n"),
            "Pair #1: All you need is love!",
        )
        self.assertEqual(
            run_script("uva_10193-hand.py", "1\n11\n101\n"),
            "Pair #1: Love is not all you need!",
        )

    def test_uva_10221(self) -> None:
        self.assertEqual(
            self.uva_10221.solve("0 180 deg\n"),
            "20231.856689 12880.000000",
        )
        self.assertEqual(
            run_script("uva_10221-hand.py", "700 60 min\n"),
            "124.616509 124.614927",
        )

    def test_uva_10222(self) -> None:
        self.assertEqual(self.uva_10222.solve("JR;;P\n"), "HELLO")
        self.assertEqual(run_script("uva_10222-hand.py", "O S,\n"), "I AM")


if __name__ == "__main__":
    unittest.main()
