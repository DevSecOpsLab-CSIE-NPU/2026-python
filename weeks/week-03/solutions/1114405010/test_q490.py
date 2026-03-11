"""q490_hand.py 的單元測試。"""

import unittest

import q490_hand as q490


class TestQ490(unittest.TestCase):
    def test_hello_world(self) -> None:
        sample_input = "HELLO\nWORLD\n"
        expected = "WH\nOE\nRL\nLL\nDO"
        self.assertEqual(q490.solve(sample_input), expected)

    def test_with_spaces(self) -> None:
        sample_input = "ABC\nD\n"
        expected = "DA\n B\n C"
        self.assertEqual(q490.solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
