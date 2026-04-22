import unittest

from test_utils import load_module, run_script


class TestUVA10252(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10252.py")
        cls.easy = load_module("uva_10252-easy.py")

    def test_sample_case(self) -> None:
        raw_input = """1
3
0 0
1 1
2 2
"""
        expected = "4 1"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_even_points_have_multiple_optima(self) -> None:
        raw_input = """1
4
0 0
0 1
2 0
2 1
"""
        expected = "6 6"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10252.py", "1\n1\n5 7\n")
        self.assertEqual(output, "0 1")


if __name__ == "__main__":
    unittest.main()
