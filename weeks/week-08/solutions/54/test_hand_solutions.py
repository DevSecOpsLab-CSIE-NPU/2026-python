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
        raw_input = "1 1\n*\n0 0\n"
        self.assertEqual(self.uva_10189.solve(raw_input), "Field #1:\n*")
        self.assertEqual(run_script("uva_10189-hand.py", raw_input), "Field #1:\n*")

    def test_uva_10190(self) -> None:
        self.assertEqual(self.uva_10190.solve("3 81\n"), "81 27 9 3 1")
        self.assertEqual(run_script("uva_10190-hand.py", "3 8\n"), "Boring!")

    def test_uva_10193(self) -> None:
        raw_input = "1\n10\n11\n"
        expected = "Pair #1: Love is not all you need!"
        self.assertEqual(self.uva_10193.solve(raw_input), expected)
        self.assertEqual(run_script("uva_10193-hand.py", raw_input), expected)

    def test_uva_10221(self) -> None:
        out = self.uva_10221.solve("500 30 deg\n")
        self.assertEqual(out, "3633.775503 3592.408346")
        self.assertEqual(run_script("uva_10221-hand.py", "700 60 min\n"), "124.616509 124.614927")

    def test_uva_10222(self) -> None:
        self.assertEqual(self.uva_10222.solve("y\n"), "t")
        self.assertEqual(run_script("uva_10222-hand.py", "Y U\n"), "T Y")


if __name__ == "__main__":
    unittest.main()
