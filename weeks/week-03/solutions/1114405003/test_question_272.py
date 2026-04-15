import unittest

from question_272 import solve


class TestQuestion272(unittest.TestCase):
    def test_quote_replacement(self) -> None:
        self.assertEqual(
            solve('"To be or not to be," quoth the bard, "that is the question."\n'),
            "``To be or not to be,'' quoth the bard, ``that is the question.''\n",
        )

    def test_multiple_lines(self) -> None:
        self.assertEqual(solve('"A"\n"B"\n'), "``A''\n``B''\n")


if __name__ == "__main__":
    unittest.main()