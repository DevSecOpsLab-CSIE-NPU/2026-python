import unittest

from question_490 import solve


class TestQuestion490(unittest.TestCase):
    def test_sample_case(self) -> None:
        self.assertEqual(
            solve("HELLO\nWORLD\n"),
            "WH\nOE\nRL\nLL\nDO",
        )

    def test_ragged_lines(self) -> None:
        self.assertEqual(solve("A\nBC\n"), "BA\nC ")


if __name__ == "__main__":
    unittest.main()