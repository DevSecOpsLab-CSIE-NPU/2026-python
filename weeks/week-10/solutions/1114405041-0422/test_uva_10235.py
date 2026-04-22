import unittest

from test_utils import load_module, run_script


class TestUVA10235(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.standard = load_module("uva_10235.py")
        cls.easy = load_module("uva_10235-easy.py")

    def test_sample_cases(self) -> None:
        raw_input = """3
6 3
1 1 1
1 0 1
1 1 1
1 1 1
1 0 1
1 1 1
2 4
1 1 1 1
1 1 1 1
1 1
0
"""
        expected = "Case 1: 3\nCase 2: 2\nCase 3: 1"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_simple_blocked_or_impossible(self) -> None:
        raw_input = """2
1 1
1
1 2
1 0
"""
        expected = "Case 1: 0\nCase 2: 0"
        self.assertEqual(self.standard.solve(raw_input), expected)
        self.assertEqual(self.easy.solve(raw_input), expected)

    def test_command_line_execution(self) -> None:
        output = run_script("uva_10235.py", "1\n1 1\n0\n")
        self.assertEqual(output, "Case 1: 1")


if __name__ == "__main__":
    unittest.main()
