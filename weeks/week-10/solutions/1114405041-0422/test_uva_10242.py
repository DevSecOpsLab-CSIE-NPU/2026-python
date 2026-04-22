import unittest

from test_utils import load_module, run_script


class TestUVA10242(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10242.py")
        cls.easy = load_module("uva_10242-easy.py")

    def test_sample_case(self) -> None:
        raw_input = """6 7
1 2
2 3
3 5
2 4
4 1
2 6
6 5
10
12
8
16
1
5
1 4
4 3 5 6
"""
        expected = "47"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_simple_chain(self) -> None:
        raw_input = """3 2
1 2
2 3
5
6
7
1 1
3
"""
        expected = "18"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        output = run_script(
            "uva_10242.py",
            "2 1\n1 2\n3\n4\n1 1\n2\n",
        )
        self.assertEqual(output, "7")


if __name__ == "__main__":
    unittest.main()
