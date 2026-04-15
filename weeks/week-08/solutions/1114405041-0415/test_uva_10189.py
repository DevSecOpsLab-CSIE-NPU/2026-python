import unittest

from test_utils import load_module, run_script


SAMPLE_INPUT = """4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
"""

SAMPLE_OUTPUT = """Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100"""


class TestUVA10189(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10189.py")
        cls.easy = load_module("uva_10189-easy.py")

    def test_sample_cases(self) -> None:
        self.assertEqual(self.standard.solve(SAMPLE_INPUT), SAMPLE_OUTPUT)
        self.assertEqual(self.easy.solve(SAMPLE_INPUT), SAMPLE_OUTPUT)

    def test_no_mine_case(self) -> None:
        raw_input = "1 3\n...\n0 0\n"
        expected = "Field #1:\n000"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10189.py", "1 1\n*\n0 0\n")
        self.assertEqual(output, "Field #1:\n*")


if __name__ == "__main__":
    unittest.main()
