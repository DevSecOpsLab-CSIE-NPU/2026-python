import unittest

from test_utils import load_module, run_script


class TestUVA10226(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10226.py")
        cls.easy = load_module("uva_10226-easy.py")

    def test_sample_cases(self) -> None:
        raw_input = """3
0
0
0
3
1 0
3 0
0
"""
        expected = "\n".join(
            [
                "ABC",
                "CB",
                "BAC",
                "CA",
                "CAB",
                "BA",
                "",
                "BAC",
                "CA",
                "CBA",
            ]
        )
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_small_custom_case(self) -> None:
        raw_input = """2
2 0
0
"""
        expected = "AB"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10226.py", "1\n0\n")
        self.assertEqual(output, "A")


if __name__ == "__main__":
    unittest.main()
