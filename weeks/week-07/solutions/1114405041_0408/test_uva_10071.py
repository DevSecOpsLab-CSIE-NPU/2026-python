import unittest

from test_utils import load_module, run_script


class TestUVA10071(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10071.py")
        cls.easy = load_module("uva_10071-easy.py")

    def test_multiple_rows(self) -> None:
        raw_input = "0 0\n1 2\n-1 2\n"
        expected = "0\n4\n-4"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_formula_helper(self) -> None:
        self.assertEqual(self.standard.displacement_after_round_trip(5, 12), 120)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10071-easy.py", "3 7\n")
        self.assertEqual(output, "42")


if __name__ == "__main__":
    unittest.main()