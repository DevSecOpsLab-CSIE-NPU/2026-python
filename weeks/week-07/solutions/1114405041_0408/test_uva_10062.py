import unittest

from test_utils import load_module, run_script


class TestUVA10062(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10062.py")
        cls.easy = load_module("uva_10062-easy.py")

    def test_single_case_sorting_rule(self) -> None:
        expected = "67 1\n66 2\n65 3"
        self.assertEqual(self.standard.solve("AAABBC\n"), expected)
        self.assertEqual(self.easy.solve("AAABBC\n"), expected)

    def test_multiple_cases_with_blank_separator(self) -> None:
        raw_input = "AAABBC\n122333\n"
        expected = "67 1\n66 2\n65 3\n\n49 1\n50 2\n51 3"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10062.py", "Aab\n")
        self.assertEqual(output, "98 1\n97 1\n65 1")


if __name__ == "__main__":
    unittest.main()