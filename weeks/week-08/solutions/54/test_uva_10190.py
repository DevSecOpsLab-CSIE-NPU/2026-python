import unittest

from test_utils import load_module, run_script


class TestUVA10190(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10190.py")
        cls.easy = load_module("uva_10190-easy.py")

    def test_known_cases(self) -> None:
        raw_input = "3 81\n3 8\n5 125\n"
        expected = "81 27 9 3 1\nBoring!\n125 25 5 1"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_helper(self) -> None:
        self.assertEqual(self.standard.build_sequence(2, 1), "Boring!")
        self.assertEqual(self.standard.build_sequence(3, 81), "81 27 9 3 1")

    def test_command_line_execution(self) -> None:
        self.assertEqual(run_script("uva_10190.py", "3 81\n"), "81 27 9 3 1")


if __name__ == "__main__":
    unittest.main()
