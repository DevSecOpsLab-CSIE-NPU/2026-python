import unittest

from test_utils import load_module, run_script


class TestUVA10189(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10189.py")
        cls.easy = load_module("uva_10189-easy.py")

    def test_sample_cases(self) -> None:
        raw_input = (
            "4 4\n"
            "*...\n"
            "....\n"
            ".*..\n"
            "....\n"
            "3 5\n"
            "**...\n"
            ".....\n"
            ".*...\n"
            "0 0\n"
        )
        expected = (
            "Field #1:\n"
            "*100\n"
            "2210\n"
            "1*10\n"
            "1110\n\n"
            "Field #2:\n"
            "**100\n"
            "33200\n"
            "1*100"
        )
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        raw_input = "1 1\n.\n0 0\n"
        self.assertEqual(run_script("uva_10189.py", raw_input), "Field #1:\n0")


if __name__ == "__main__":
    unittest.main()
