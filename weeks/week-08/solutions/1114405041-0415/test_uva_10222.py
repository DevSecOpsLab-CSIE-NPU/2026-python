import unittest

from test_utils import load_module, run_script


class TestUVA10222(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10222.py")
        cls.easy = load_module("uva_10222-easy.py")

    def test_decode_sentence(self) -> None:
        raw_input = "O S, GOMR YPFSU/\n"
        expected = "I AM FINE TODAY."
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_keep_spaces_and_multiple_lines(self) -> None:
        raw_input = "O   S,\nJR;;P\n"
        expected = "I   AM\nHELLO"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10222.py", "JR;;P\n")
        self.assertEqual(output, "HELLO")


if __name__ == "__main__":
    unittest.main()
