import unittest

from test_utils import load_module, run_script


class TestUVA10193(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10193.py")
        cls.easy = load_module("uva_10193-easy.py")

    def test_sample_style_cases(self) -> None:
        raw_input = "3\n10\n110\n101\n1000\n1111\n0011\n"
        expected = (
            "Pair #1: All you need is love!\n"
            "Pair #2: Love is not all you need!\n"
            "Pair #3: All you need is love!"
        )
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10193.py", "1\n11\n101\n")
        self.assertEqual(output, "Pair #1: Love is not all you need!")


if __name__ == "__main__":
    unittest.main()
