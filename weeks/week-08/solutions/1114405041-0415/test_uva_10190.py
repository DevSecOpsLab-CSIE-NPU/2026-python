import unittest

from test_utils import load_module, run_script


class TestUVA10190(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10190.py")
        cls.easy = load_module("uva_10190-easy.py")

    def test_valid_and_boring_cases(self) -> None:
        raw_input = "81 3\n100 10\n5 1\n31 2\n"
        expected = "81 27 9 3 1\n100 10 1\nBoring!\nBoring!"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_single_valid_case(self) -> None:
        self.assertEqual(self.standard.solve("27 3\n"), "27 9 3 1")
        self.assertEqual(self.easy.solve("27 3\n"), "27 9 3 1")

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10190.py", "64 4\n")
        self.assertEqual(output, "64 16 4 1")


if __name__ == "__main__":
    unittest.main()
