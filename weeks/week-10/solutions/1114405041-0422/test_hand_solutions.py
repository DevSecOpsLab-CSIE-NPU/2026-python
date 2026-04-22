import unittest

from test_utils import load_module, run_script


class TestHandSolutions(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.uva_10226 = load_module("uva_10226-hand.py")
        cls.uva_10235 = load_module("uva_10235-hand.py")
        cls.uva_10242 = load_module("uva_10242-hand.py")
        cls.uva_10252 = load_module("uva_10252-hand.py")
        cls.uva_10268 = load_module("uva_10268-hand.py")

    def test_uva_10226(self) -> None:
        self.assertEqual(self.uva_10226.solve("1\n0\n"), "A")
        self.assertEqual(run_script("uva_10226-hand.py", "2\n2 0\n0\n"), "AB")

    def test_uva_10235(self) -> None:
        self.assertEqual(self.uva_10235.solve("1\n1 1\n0\n"), "Case 1: 1")
        self.assertEqual(run_script("uva_10235-hand.py", "1\n1 1\n1\n"), "Case 1: 0")

    def test_uva_10242(self) -> None:
        self.assertEqual(
            self.uva_10242.solve("2 1\n1 2\n3\n4\n1 1\n2\n"),
            "7",
        )
        self.assertEqual(run_script("uva_10242-hand.py", "1 0\n5\n1 1\n1\n"), "5")

    def test_uva_10252(self) -> None:
        self.assertEqual(self.uva_10252.solve("1\n1\n3 4\n"), "0 1")
        self.assertEqual(run_script("uva_10252-hand.py", "1\n2\n0 0\n2 0\n"), "2 3")

    def test_uva_10268(self) -> None:
        self.assertEqual(self.uva_10268.solve("1 1\n0 0\n"), "1")
        self.assertEqual(run_script("uva_10268-hand.py", "1 2\n0 0\n"), "2")


if __name__ == "__main__":
    unittest.main()
