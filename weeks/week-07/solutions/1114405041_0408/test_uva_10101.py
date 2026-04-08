import unittest

from test_utils import load_module, run_script


class TestUVA10101(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10101.py")
        cls.easy = load_module("uva_10101-easy.py")

    def test_format_helper(self) -> None:
        self.assertEqual(self.standard.format_bangla_number(0), "0")
        self.assertEqual(self.standard.format_bangla_number(10000000), "1 kuti")
        self.assertEqual(
            self.standard.format_bangla_number(123456789),
            "12 kuti 34 lakh 56 hajar 7 shata 89",
        )

    def test_full_solve_output(self) -> None:
        raw_input = "0\n1\n10000000\n123456789\n"
        expected = "   1. 0\n   2. 1\n   3. 1 kuti\n   4. 12 kuti 34 lakh 56 hajar 7 shata 89"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10101-easy.py", "100000000\n")
        self.assertEqual(output, "   1. 10 kuti")


if __name__ == "__main__":
    unittest.main()