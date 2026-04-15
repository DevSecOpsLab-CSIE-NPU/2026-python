import unittest

from test_utils import load_module, run_script


class TestUVA10222(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10222.py")
        cls.easy = load_module("uva_10222-easy.py")

    def test_decode_sentence(self) -> None:
        raw_input = "y;u\n"
        expected = "tly"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_keep_space_and_unknown(self) -> None:
        raw_input = "Y U\n"
        expected = "T Y"
        self.assertEqual(self.standard.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        self.assertEqual(run_script("uva_10222.py", "y\n"), "t")


if __name__ == "__main__":
    unittest.main()
