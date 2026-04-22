import unittest

from test_utils import load_module, run_script


class TestUVA10268(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10268.py")
        cls.easy = load_module("uva_10268-easy.py")

    def test_sample_cases(self) -> None:
        raw_input = """2 100
10 786599
4 786599
60 1844674407370955161
63 9223372036854775807
0 0
"""
        expected = "\n".join(
            [
                "14",
                "21",
                "More than 63 trials needed.",
                "61",
                "63",
            ]
        )
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_small_cases(self) -> None:
        raw_input = """1 1
1 2
2 2
0 0
"""
        expected = "1\n2\n2"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10268.py", "1 3\n0 0\n")
        self.assertEqual(output, "3")


if __name__ == "__main__":
    unittest.main()
